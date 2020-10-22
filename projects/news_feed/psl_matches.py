"""
    Script for extracting data of PSL 2019 matches
    :file: psl_matches.py
    :platform: Windows 10
    :synopsis:
        This script first uses request function to open the
        intended psl website and saves the links of all psl
        matches in a list. After this, it grabs all the
        information (including teams, their scores and result)
        from the website and store it in their relevant lists.
        At last, this script displays all the information in
        tabular form using pandas data frame.

    :author:
        Muhammad Faheem-ur-Rehman
        email: faheemlasani1034@gmail.com
"""

# importing required libraries
import pandas as pd
import utilities


def main():
    """
        main function
    """
    print('Fetching PSL 2020 matches data. Please wait ...')

    # calling function to grab match number, venue and date
    match_number, match_venue, match_date = utilities.grab_match_number_date_venue("small mb-0 match-description")

    # calling function to grab the team names
    team_a, team_b = utilities.grab_team_names('row no-gutters', 'name')

    # calling function to grab the team scores
    team_a_score, team_b_score = utilities.grab_team_scores('row no-gutters', 'score')

    # calling function to grab the name of winning team
    winning_team = utilities.grab_winning_team('extra-small mb-0 match-description match-description-bottom')

    # rearranging all fetched data into tabular form
    all_fetched_information = list()
    for match_no, match_Date, match_place, team1, team2, \
        team1_score, team2_score, winner \
            in zip(match_number, match_date, match_venue, team_a,
                   team_b, team_a_score, team_b_score, winning_team):
        all_fetched_information.append(
            {'Match Number': match_no, 'Date': match_Date, 'Venue': match_place, ' Team A': team1,
             'Team B': team2, ' A score': team1_score, ' B score': team2_score, '  Result  ': winner})

    pandas_data_frame = pd.DataFrame(all_fetched_information)

    # printing all fetched information
    print(pandas_data_frame.to_string())

    # calling function to create the psl_json_data file and saving it in separate data folder
    utilities.creating_psl_json_file(all_fetched_information)


if __name__ == '__main__':
    main()
