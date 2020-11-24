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
import simplejson
import os


def create_psl_url(calendar_year):
    """
    Function returning back specific year url of PSL

    :param string calendar_year: Calendar year for which PSL url is required

    :return: PSL matches url of a requested calendar year
    :rtype: string
    """
    return "https://www.espncricinfo.com/scores/series/8679/season/{}/pakistan-super-league?view=results".format(
        calendar_year)


def create_soup_from_url(url_link):
    """
    Function for grabbing URL data and converting it into soup object

    :param string url_link: URL link containing PSL matches data

    :return: BS for url link
    :rtype: Soup Class Object
    """
    # requesting to access PSL website and making soup
    url_response = requests.get(url_link)
    src_code = url_response.content
    return BeautifulSoup(src_code, 'lxml')


def grab_match_number_date_venue(soup, class_attribute):
    """
    Function for getting number, date and venue of psl matches using soup object

    :param BS Object soup: BS Object containing data
    :param string class_attribute: Soup class name under which matches number,venue and date is placed

    :returns: matches number, their venue and date of occurrence
    :return type: list
    """
    match_number_date_venue = list()
    match_number = list()
    match_venue = list()
    match_date = list()

    number_date_venue_element = soup.find_all(class_=class_attribute)

    for item in number_date_venue_element:
        match_number_date_venue.append(item.text)

    for grabbed_information in match_number_date_venue:
        separated_information = grabbed_information.split(',')
        match_number.append(separated_information[0])
        match_venue.append(separated_information[1])
        match_date.append(separated_information[2])

    return match_number, match_venue, match_date


def grab_team_names(soup, class_attribute_general, class_attribute_specific):
    """
    Function for getting the names of playing teams using soup object

    :param BS Object soup: BS Object containing data
    :param string class_attribute_general: Soup class name under which team name is placed
    :param string class_attribute_specific: Soup class name under which team name is placed in text form

    :returns:team names
    :return type: list
    """
    team_names = list()
    team_a = list()
    team_b = list()

    for first_item in soup.find_all(class_=class_attribute_general):
        for second_item in first_item.find_all(class_=class_attribute_specific):
            team_names.append(second_item)

    for name in team_names:
        if team_names.index(name) % 2 == 0:
            team_a.append(name.text)
        else:
            team_b.append(name.text)

    return team_a, team_b


def grab_team_scores(soup, class_attribute_general, class_attribute_specific):
    """
    Function for getting the scores of  teams using soup object

    :param BS Object soup: BS Object containing data
    :param string class_attribute_general: Soup class name under which team scores are placed
    :param string class_attribute_specific: Soup class name under which team scores are placed in text form

    :returns:team scores
    :return type: list
    """
    team_scores = list()
    team_a_score = list()
    team_b_score = list()

    for first_item in soup.find_all(class_=class_attribute_general):
        for second_item in first_item.find_all(class_=class_attribute_specific):
            team_scores.append(second_item.text)

    for score in team_scores:
        if team_scores.index(score) % 2 == 0:
            team_a_score.append(score)
        else:
            team_b_score.append(score)

    return team_a_score, team_b_score


def grab_winning_team(soup, class_attribute):
    """
     Function for getting the names winning using soup object

    :param BS Object soup: BS Object containing data
    :param string class_attribute: Soup class name under which winning team name is placed

    :returns:winning team
    :return type: list
    """
    winning_team = list()
    winning_team_element = soup.find_all(class_=class_attribute)

    for item in winning_team_element:
        winning_team.append(item.text)

    return winning_team


def creating_psl_json_file(fetched_information):
    """
    Function for converting the fetched information into json file format and saving it
    in a separate data folder

    :param list fetched_information: Contains information of all psl 2019 matches

    :returns: None
    """

    psl_json_data = simplejson.dumps(fetched_information)
    data_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

    if not os.path.exists(data_folder_path):
        os.mkdir(data_folder_path)
    psl_json_data_file_path = os.path.join(data_folder_path, "psl_json_data_file.json")

    psl_json_data_file = open(psl_json_data_file_path, 'w')
    psl_json_data_file.write(psl_json_data)

    print("PSL matches data saved in {}".format('psl_json_data_file'))
