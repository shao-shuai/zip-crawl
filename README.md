# zip-crawl

## Introduction

- This script is used to crawl jobs posted on ZipRecruiter.

- This script takes two arguments, the first argument is the **keyword** **(e.g., java)** you want to search on ZipRecruiter, the second argument is the **number of pages (e.g., 10)** you want to crawl. 
- Each page has approximately 20 job postings.

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

## Step 3: Run the script `zip-crawler.py`

```
python3 zip_crawler.py java 10
```

