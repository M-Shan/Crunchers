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

# requesting to access PSL website
URL_RESPONSE = requests.get(PSL_URL_REQUEST)
SOURCE_CODE = URL_RESPONSE.content

# creating Beautiful siup object
SOUP = BeautifulSoup(SOURCE_CODE, 'lxml')


def grab_match_number_date_venue(class_attribute):
    """
       Function for getting number, date and venue of psl matches using soup object

       :param string class_attribute: Soup class name under which matches number,venue and date is placed

       :returns: matches number, their venue and date of occurrence
       :return type: list
    """
    match_number_date_venue = list()
    match_number = list()
    match_venue = list()
    match_date = list()

    number_date_venue_element = SOUP.find_all(class_=class_attribute)

    for item in number_date_venue_element:
        match_number_date_venue.append(item.text)

    for index in range(0, 30):
        grabbed_information = match_number_date_venue[index]
        separated_information = grabbed_information.split(',')
        match_number.append(separated_information[0])
        match_venue.append(separated_information[1])
        match_date.append(separated_information[2])

    return match_number, match_venue, match_date


def grab_team_names(class_attribute_general, class_attribute_specific):
    """
    Function for getting the names of playing teams using soup object

    :param string class_attribute_general: Soup class name under which team name is placed
    :param string class_attribute_specific: Soup class name under which team name is placed in text form

    :returns:team names
    :return type: list
    """
    team_names = list()
    team_a = list()
    team_b = list()
    # teams_element = soup.find_all(class_='row no-gutters')

    for first_item in SOUP.find_all(class_=class_attribute_general):
        for second_item in first_item.find_all(class_=class_attribute_specific):
            team_names.append(second_item)

    for index in range(0, 60):
        if index % 2 == 0:
            team_a.append(team_names[index].text)
        else:
            team_b.append(team_names[index].text)

    return team_a, team_b


def grab_team_scores(class_attribute_general, class_attribute_specific):
    """
    Function for getting the scores of  teams using soup object

    :param string class_attribute_general: Soup class name under which team scores are placed
    :param string class_attribute_specific: Soup class name under which team scores are placed in text form

    :returns:team scores
    :return type: list
    """
    team_scores = list()
    team_a_score = list()
    team_b_score = list()

    for first_item in SOUP.find_all(class_=class_attribute_general):
        for second_item in first_item.find_all(class_=class_attribute_specific):
            team_scores.append(second_item.text)

    for index in range(0, 60):
        if index % 2 == 0:
            team_a_score.append(team_scores[index])
        else:
            team_b_score.append(team_scores[index])

    return team_a_score, team_b_score


def grab_winning_team(class_attribute):
    """
     Function for getting the names winning using soup object

    :param string class_attribute: Soup class name under which winning team name is placed

    :returns:winning team
    :return type: list
    """
    winning_team = list()
    winning_team_element = SOUP.find_all(class_=class_attribute)

    for item in winning_team_element:
        winning_team.append(item.text)

    return winning_team
