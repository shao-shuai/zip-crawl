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

def process_url(url):
	"""
	This function takes a url as input, and write the url and the content to a 
	txt file
	"""
	path = input('Please input saving path: ')
	if not os.path.exists(path):
		os.mkdir(path)

	filename = input('Please input filename (with file extension): ')
	path = path + '/' + filename

	response = requests.get(url).content
	soup = BeautifulSoup(response, 'lxml')

	title_div = soup.findAll("h1", {"class": "job_title"})
	title = {'Title':list(title_div[0].stripped_strings)[0]}

	company_div = soup.findAll("div", {"class": "job_location"})
	company = dict(zip(['Company', 'Location'], list(company_div[0].stripped_strings)))

	job_desc = soup.findAll("article", {"id":"job_desc"})
	descs = list(job_desc[0].stripped_strings)

	# Write content of link to txt file
	job_info = {**title, **company}

	with open(path, 'w', encoding='utf8') as file:
		file.write('%s\n\n' % ('url: '+ url))
		for key, value in job_info.items():
			file.write('%s: %s\n' % (key, value))
		file.write('\n')	
		for desc in descs:
			file.write('%s\n' % desc)

def main():

	process_url(sys.argv[1])

	logging.info('Writing job infomation of %s' % (sys.argv[1]))

if __name__ == "__main__":

	main()
	
    

