from bs4 import BeautifulSoup as Bs
import requests
import csv
import pandas as pd

url = 'https://trojanconstruction.group/en/projects/COMPLETED'
html_trojan = requests.get(url).text
soup = Bs(html_trojan,'html5lib')
# print(soup.prettify())

project_container = soup.find_all('div',class_='projects_img')
file = 'projects_data.csv'
csv_file = open(file,'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Project Name','Project Image link'])
for item in project_container:
    project_img = item.find('img')['src'].strip()
    project_name = item.find('h2').text
    # project_name

    # print(project_name,"|",project_img)
    csv_writer.writerow([project_name,project_img])
csv_file.close()