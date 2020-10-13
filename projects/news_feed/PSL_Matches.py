"""
    Script for saving the links of all PSL 2019 matches
    :file: psl_matches.py
    :platform: Windows 10
    :synopsis:
        This script first uses request function to open the
        intended psl website. After this, it uses beautiful
        soup object to extract the source code of web page.
        In the end, it uses specific classes to store the
        links of matches in a list called matches_linl[]
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
    all_matches_link = list()

    # get psl matches links
    psl_matches_links = utilities.grab_psl_matches_urls("match-highlight border-bottom", "lxml")

    if not psl_matches_links:
        raise RuntimeError('No PSL matches link found')

        # creating a data frame using pandas library
    for links in zip(psl_matches_links):
        all_matches_link.append({'Links For Matches': links})

    df = pd.DataFrame(all_matches_link)

    # printing the links of all matches shown on web page
    print(df)


if __name__ == '__main__':
    main()
