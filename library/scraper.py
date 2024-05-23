from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
from utils import text_to_list, extract_names

def getPage(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    return soup


def scrape(soup):
    """""I want to get: course title, term, instructor name, list of TAs"""
    course_title = soup.find('h1').text
    term = soup.find('h2').text
    
    ul1 = soup.find('ul')
    ul1_text = ul1.text
    ul1_list = text_to_list(ul1_text)    
    
    time = ul1_list[0]
    location = ul1_list[1]
    instructor = ' '.join(ul1_list[2].split()[1:-1])
    instructor = instructor[:-1]
    ta_list = extract_names(ul1_list, key_str = 'Course Assistants:')
    return course_title, term, time, location, instructor, ta_list
    