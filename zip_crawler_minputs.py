import os
import random
import re
import sys
from datetime import date, datetime, timedelta
from time import sleep, time
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')

def process_article(article, keyword, directory, index, search_location, path, job_location, postings):
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

	file_name = path + "{:010d}".format(index) + '_' + \
				keyword + '_' + \
				search_location + '_' + \
				title['Title'].replace('/', ' ') + '_' + \
				company['Company'] + '_' + \
				company['Location'] + '_' + \
				str(datetime.now().date()) + '.txt'

	if job_location and job_location.lower() in company['Location'].lower():	  			
		with open(file_name, 'w', encoding='utf8') as file:
			file.write('%s\n\n' % ('url: '+ job_link))
			for key, value in job_info.items():
				file.write('%s: %s\n' % (key, value))
			file.write('\n')	
			for desc in descs:
				file.write('%s\n' % desc)
	else:
		with open(file_name, 'w', encoding='utf8') as file:
			file.write('%s\n\n' % ('url: '+ job_link))
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
	key_word  = sys.argv[1]
	directory = sys.argv[2]

	path = os.getcwd() + '/' + directory + '/'
	if not os.path.exists(path):
		os.mkdir(path)

	try:
		location = sys.argv[3]
	except IndexError:
		location = None

	try:
		postings = sys.argv[4]
	except IndexError:
		postings = 50

	logging.info(f'You are scraping job postings with KEY WORD {key_word}')

	base_url = 'https://www.ziprecruiter.com/'

	pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

	match = pattern.match(base_url)

	search_location = match[2]

	links = (base_url + 'Jobs/' + \
			str(key_word) + '/' + \
			str(page) for page in range(1, 26))

	articles = []

	for link in links:
		articles = articles + process_link(link)

	for index in range(len(articles)):
		if len(os.listdir(path)) == int(postings):
			break
		try:
			process_article(articles[index], key_word, directory, index, search_location, path, location, postings)
		except IndexError: # IndexError happens when position no longer exists
			pass
		sleep(random.randint(2,6)) # Sleep random time to avoid anti-crawler

if __name__ == "__main__":
	main()
