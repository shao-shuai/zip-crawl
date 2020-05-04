# zip-crawl

## Introduction

- This script is used to crawl jobs posted on ZipRecruiter.

- Each page for a search has approximately 20 job postings.
- I tested searching **java** and **python**, each search returned 25 pages, no more.

## Getting started

## Step 1: Clone repository to local machine
```
git clone https://github.com/shao-shuai/zip-crawl.git
```

## Step 2: Create python virtual environment
```
python3 -m venv venv             # create virtualenv
source venv/bin/activate         # activate virtualenv
pip install -r requirements.txt  # install requirements
```

## Step 3: Run script

- **zip_crawler.py** takes 2 arguments, the first argument is the **keyword** (e.g., java) you want to search on ZipRecruiter, the second argument is **the number of pages** (e.g., 1-25) you want to crawl

  ```python
  python3 zip_crawler.py java 10
  ```

- **zip_crawler_url.py**

  ```shell
  python3 zip_crawler_url.py 'https://www.ziprecruiter.com/c/CyberCoders/Job/Sr.-Backend-Engineer-Python-&-AWS-Azure-GCP-100-REMOTE!/-in-Redwood-City,CA?jid=DQ10301beeda6fa0a85bd8b3abddec6a60&job_id=1dc2e1fe2f8dc47041fcda53050882f4'
  Please input saving path: ./output
  Please input filename (with file extension): test.txt
  ```

- **zip_crawler_minputs.py** - example

  ```shell
  python3 zip_crawler_minputs.py 
  Please input a keyword: python 
  Please input a folder name: python
  Please input job location: 
  Please input nubmer of postings to crawl: 
  ```

  ```shell
  python3 zip_crawler_minputs.py 
  Please input a keyword: java
  Please input a folder name: test
  Please input job location: 
  Please input nubmer of postings to crawl: 9
  ```

  ```shell
  python3 zip_crawler_minputs.py 
  Please input a keyword: java
  Please input a folder name: java
  Please input job location: san francisco
  Please input the nubmer of postings to crawl: 3
  ```

  

