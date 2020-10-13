"""
    This script involves variables and specific functions
    that will be utilized in main file (psl_matches)
    :file: utilities.py
    :platform: windows 10
    :synopsis:
        Script containing common variables and functions
    :author:
        Muhammad Faheem ur Rehman
        email: faheemlasani1034@gmail.com
"""

# importing required libraries
import requests
from bs4 import BeautifulSoup

# global variables to use
PSL_URL_REQUEST = "https://www.espncricinfo.com/scores/series/8679/season/2020/pakistan-super-league?view=results"


def grab_psl_matches_urls(class_attribute, soup_layout_format):
    """
       Function for getting a specific urls of psl matches using soup object

       :param string class_attribute: Soup class name under which matches link is placed
       :param string soup_layout_format: Soup reading format

       :returns: list containig the links of all psl matches
       :return type: list
       """

    url_response = requests.get(PSL_URL_REQUEST)
    source_code = url_response.content

    # making BeautifulSoup object using previously grabbed source code
    soup = BeautifulSoup(source_code, soup_layout_format)

    matches_links = list()

    # storing the links of results of all matches(read from the web) in a list called matches_links
    for matches_data in soup.find_all(class_=class_attribute):
        matches = matches_data.find('a')
        matches_links.append(matches.attrs['href'])

    return matches_links
