"""
This module implements a basic consumer for demonstration purposes using python 'requests' package.
The main objective of this module is demonstrate basic http operations acting as a REST API consumer.

References:
https://requests.readthedocs.io
https://requests.readthedocs.io/en/latest/api/#requests.Response
"""

import requests
import logging
import json
import os
from pprint import pp
from aimodule import summarize, get_tokens



# Global variables
TOKEN = os.getenv('SECRET_TOKEN')
BASE_URL = "http://vps-b30e981b.vps.ovh.net:50005/api/v1"
HEADERS = {'Content-Type': 'application/json', 'Authorization': f"Bearer {TOKEN}"}


def get_basic(endpoint):
    """
    Performs a simple GET operation passing only an API endpoint 
    """

    url = BASE_URL + f"{endpoint}"
    r = requests.get(url)    
    
    response = r.json()
    return response


def summarize_complain(id):
    """
    Get a complain by id and summarize the text
    """
    endpoint = f"/complain/{id}"
    complain = get_basic(endpoint)
    complain_text = complain.get('text')
    complain_summarized = summarize(complain_text)
    return {'complain_id': id, 'summary': complain_summarized}


def complains_overview(brand):
    endpoint =f"/complain/brands/complains/text?brand={brand}"
    get_all_complains = get_basic(endpoint)
    dump_complains_text = get_all_complains.get('text')
    complains = ";".join(dump_complains_text)
    print(get_tokens(complains).nb_tokens)
    complains_summarized = summarize(complains)
    return complains

pp(complains_overview('wizink'))
