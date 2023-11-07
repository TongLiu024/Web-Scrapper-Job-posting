
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import Xlsxwriter


def find_jobs():
    html_content = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    # Beautifulsoup Constructor (:param markup: A string or a file-like object representing markup to be parsed.)
    # :param features: Desirable features of the parser to be used , This may be the name of a specific parser ("lxml", "lxml-xml", "html.parser", or "html5lib")
    print("Filtering out unfamiliar skills:")
    print("please enter the skillset that you are not familiar with:")
    unfamiliar_skills = input(">")

    soup = BeautifulSoup(html_content, 'lxml')
    # find() will only return the first element found
    job_list = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(job_list):

        company_name = job.find(
            "h3", class_="joblist-comp-name").text
        required_skills = job.find(
            "span", class_='srp-skills').text.replace(" ", "")

        posting_date = job.find('span', class_="sim-posted").span.text
        link_for_more_info = job.header.h2.a['href']
        if unfamiliar_skills not in required_skills:

            with open(f"Job posting {index}.txt", "w") as f:
                f.write(f"Job posting date: {posting_date.strip()}\n")
                f.write(f"Company name: {company_name.strip()}\n")
                f.write(f"Required skillsets: {required_skills.strip()}\n")
                f.write(f"Link for more info: {link_for_more_info}\n")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
