import os
import os
import random
import re
import sys
from collections import OrderedDict
from datetime import date, datetime, timedelta
from time import sleep, time
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')

def process_article(article, keyword):
	"""
	- This function takes an article as input, each article
	is a job posting in the search result

	- Job info including title, job description will be extracted 
	and write to a txt file
	"""
	title_div = article.findAll("span", {"class": "just_job_title"})
	title = {'Title':list(title_div[0].stripped_strings)[0]}

	company_div = article.findAll("p", {"class": "job_org"})
	company = dict(zip(['Company', 'Location'], list(company_div[0].stripped_strings)))

	job_div = article.findAll("section", {"class": "perks_item"})
	job_type = list(job_div[0].stripped_strings)
	job_type_dict = {job_type[0]:job_type[1]}

	job_snippet = article.findAll("p", {"class": "job_snippet"})
	job_link = job_snippet[0].findAll("a")[0]['href'] # this link refers to the individual page of each job posting
	job_page = requests.get(job_link).content
	job_soup = BeautifulSoup(job_page, 'lxml')
	job_desc = job_soup.findAll("article", {"id":"job_desc"})
	descs = list(job_desc[0].stripped_strings)

	logging.info(f'Processing {job_link} now.......\n')

	# Write job information into txt file
	job_info = {**title, **company, **job_type_dict}
	file_name = './dataset/' + keyword + '_' + str(datetime.now().timestamp()) + '.txt'
	with open(file_name, 'w', encoding='utf8') as file:
		for key, value in job_info.items():
			file.write('%s: %s\n' % (key, value))
		file.write('\n')	
		for desc in descs:
			file.write('%s\n' % desc)

def process_link(link):
	"""
	This function will take a link as input, and return a list of articles, 
	each artile is a unique job posting
	"""
	response = requests.get(link).content
	page = BeautifulSoup(response, 'lxml')
	articles = page.find_all("article")

	return articles

def main():
	start_time = time()

	key_word = sys.argv[1]

	pages = int(sys.argv[2])

	logging.info(f'You are scraping job postings with KEY WORD {key_word} in {pages} page(s)')

	links = ('https://www.ziprecruiter.com/Jobs/' + str(key_word) + '/' + str(page) for page in range(1, pages + 1))

	articles = []

	for link in links:
		articles = articles + process_link(link)

	logging.info(f'The total number of articles to scrape is {len(articles)}.')

	for article in articles:
		try:
			process_article(article, key_word)
		except IndexError: # IndexError happens when position no longer exists
			pass
		sleep(random.randint(6,10)) # Sleep random time from 6s to 10s to avoid anti-crawler

	jobs = len(os.listdir('./dataset'))
	
	logging.info(f'Crawled {jobs} job in {time() - start_time} seconds')

if __name__ == "__main__":

	main()
	
    

