# Wuzzuf Web Scraping Task

## Objective

Use **Python + Selenium** to scrape job data from Wuzzuf.

### Website

Wuzzuf: https://wuzzuf.net/

Search for:

```text
Data Engineer
Data Science 
AI Developer
Machine Learning Engineer
```

## Requirements

### 1. Scrape Job Data

Extract the following information:

* Job Title
* Company
* Location
* Job Type
* Experience
* Job URL

### 2. Pagination

Scrape jobs from **more than one page**.


### 3. Save Data

Save the scraped data into:

```text
wuzzuf_jobs.csv
```

The CSV should contain:

```text
job_title
company
location
job_type
experience
job_url
```

### 4. Remove Duplicates

Make sure duplicate jobs are removed using the `job_url`.

