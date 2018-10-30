"""""
program is a simple web scraper that scrapes the webpage of the
computer science faculty page
uses beautiful soup

Author: Chris Roach
Date: 10/29/2018
"""""
from bs4 import BeautifulSoup
import requests

#declarations
phone_list = []
prof_list = []
url = 'https://www.marshall.edu/cite/csfac/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#get the tbody element from the page, this is where all the professor information is

professor_info_table_body = soup.find("tbody")

#find all the individual professor information, skipping the first tr

professor_info_individual = professor_info_table_body.find_all("tr")[1:]

#iterate through each individual tr element and find where the professors name and title is listed
#and add it to prof_list
for individual in professor_info_individual:
    professor_name_title = individual.find("div", {"style": "float: left"})
    prof_list.append(professor_name_title.text.rstrip())

#iterate through individual tr elements and find the phone number
# of each professor and add to phone_list, if phone number is not available just add "unavailable"
for office in professor_info_individual:
    office_and_phone = office.find_all("td", {"valign": "top"})[1:]
    for office_info in office_and_phone:
        phone_office = office_info.find_all("h6")[1]
        for phone_office_stripped in phone_office:
            if 'Phone' in phone_office_stripped:
                phone_list.append(phone_office_stripped)
            else:
                phone_list.append("unavailable")

#print out all information
for i in range(len(prof_list)):
    print(prof_list[i])
    print(phone_list[i])



