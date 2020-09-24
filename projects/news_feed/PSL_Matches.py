#This code grabs the data from the suggested website
#and then stores the links of results of all matches in a list called All_Matches_Links

# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# sending my URL request
url = "https://www.espncricinfo.com/scores/series/8679/season/2020/pakistan-super-league?view=results"
url_response = requests.get(url)
source_code = url_response.content

#Making Beautifulsoup object using previously grabbed source code
soup = BeautifulSoup(source_code, 'lxml')

# making an empty list for storing matches information and an overall list to display all links in tabular form
matches_links = []
All_Matches_Links = []

# storing the links of results of all matches(read from the web) in a list called matches_links
for matches_data in soup.find_all(class_='match-highlight border-bottom'):
    matches = matches_data.find('a')
    matches_links.append(matches.attrs['href'])

#creating a data frame using pandas library
for links in zip(matches_links):
    All_Matches_Links.append({'Links For Matches': links})

df = pd.DataFrame(All_Matches_Links)

#printitng the links of all matches shown on web page
print(df)
