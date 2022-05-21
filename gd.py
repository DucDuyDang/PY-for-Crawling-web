'''import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

print(page.text)'''

import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

print(results.prettify())

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()


for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    filename = 'D:\\ADMIN\\Documents\\HỌC KÌ 4\\PYTHON\\PythonCrawlData.docx'

    file = open(filename, 'wb')
    def download(url, filename):
        with open(filename, 'wb') as file: # TẢI DATA VỀ
            respone = requests.get(title_element + company_element + location_element)
            file.write(respone.content)
            file.close()

python_jobs = results.find_all("h2", string="Python")

'''
#Phát triển thêm bằng cách đưa về file xlsx hoặc csv theo column mình muốn
#import pandas as pd
#output = pd.python_jobs({'TenViec': title_element,'Congty':company_element,'DiaDiem':location_element})
#print(output)
'''

print(python_jobs)
[]

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

print(len(python_jobs))


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    # -- snip--
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
