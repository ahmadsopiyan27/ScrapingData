

from bs4 import BeautifulSoup
import pandas as pd
import requests



# base_url = f'https://id.jobstreet.com/id/qa-automation-jobs/in-jakarta'

# response = requests.get(base_url)
# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

def scrape_jobstreet_jobs(position,location):
    position = position.lower().replace(' ', '-')
    location = location.lower().replace(' ', '-')
    base_url = f'https://id.jobstreet.com/id/{position}-jobs/in{location}'

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = [] #nnti diisi dengan data berupa dictionary job tittle, company, link

    for job_card in soup.find_all('article', {'data-testid':'job-card'}):
        try:
            job_elem = job_card.find('a', {'data-testid':'job-card-title'})
            job_title = job_card.find('a', {'data-testid':'job-card-title'}).text.strip()
            company = job_card.find('a', {'data-automation':'jobCompany'}).text.strip()
            link = job_elem['href']

            jobs.append({'title':job_title, 
                         'company':company, 
                         'job link':'https://id.jobstreet.com/id/job'+link
                         })
            
        except AttributeError:
            continue



    return jobs

job_position = input('masukin posisi yang dicari: ')
job_location = input('dimana lokasinya?: ')


job_list = scrape_jobstreet_jobs(job_position, job_location)


print(job_list)

df=pd.DataFrame(job_list)

df.to_excel('lowongan_jobstreet.xlsx', index=False)

print('udah bang!')
    
