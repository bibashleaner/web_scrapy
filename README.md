# web_scrapy

An introduction to web scraping tool/framework "Scrapy"

### Prerequisites

- Python 3.x
- pip
- [Scrapy](https://scrapy.org/)

### Installation

#Create virtual env
  -Python -m venv envirnomentName
  -For Bash
     -source .../envirnomentName/scripts/activate

#Install scrapy
  -pip install scrapy

#Start the project
  -scrapy startproject projectname

#Extract the data
  -scrapy crawl spidername

#Store the scraped data
  -scrapy crawl spidername -o jsonname.json/jsonl
