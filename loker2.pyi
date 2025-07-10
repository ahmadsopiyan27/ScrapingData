from bs4 import BeautifulSoup
import pandas as pd
import requests



base_url = f'https://id.jobstreet.com/id/qa-automation-jobs/in-jakarta'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
