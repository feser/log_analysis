# Log Analysis Project

## Purpose
* Internal reporting tool for a newspaper site that will use information from the database to discover what kind of articles the site's readers like.

### Stored Information
* Articles 
* Authors
* Access logs

### Answered Questions
* What are the most popular three articles of all time? 
* Who are the most popular article authors of all time? 
* On which days did more than 1% of requests lead to errors?

## How to run
* Install postgresql
* Create database "news"
* Download https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
* Load data with "psql -d news -f newsdata.sql" command
* Change user and password at log_analysis.py with your database user and password
* run ./log_analysis.py or python log_analysis.py
