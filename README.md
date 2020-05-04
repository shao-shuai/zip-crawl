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

- **zip_crawler_url.py** takes 2 arguments, the first is the **job link**, the second is the **filename**

  ```python
  python3 zip_crawler_url.py 'https://www.ziprecruiter.com/c/MSR-IT-Ltd/Job/Java-Hadoop-Developer/-in-San-Francisco,CA?jid=DQcb18bb95b9b8dc75e9ff573f0123c203&job_id=bb35a417b842fb07dfead7a8e18072da' sample
  ```

- **zip_crawler_minputs.py** takes multiple arguments

  ```python
  python3 zip_crawler_minputs.py <keyword> <directory name> <job location> <number of postings>
  ```

  ```python
  python3 zip_crawler_minputs.py java nihao ca 5
  ```

  