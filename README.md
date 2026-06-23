# Pakistan Job Market Scraper & Analyzer

A Python automation project that scrapes job listings, cleans the data, and generates visual insights about the Pakistani job market.

## Features

- Scrapes job listings (title, company, location, salary) from Indeed
- Cleans and standardizes raw data using pandas
- Generates 4 analysis charts automatically
- Modular code — each step is a separate, clean module

## Project Structure

```
job-scraper/
├── main.py          # Run everything in one command
├── scraper.py       # Fetches job listings from the web
├── cleaner.py       # Cleans and standardizes raw data
├── analyzer.py      # Generates charts from clean data
├── data/
│   ├── raw_jobs.csv
│   └── clean_jobs.csv
├── output/
│   └── charts/      # All generated charts saved here
└── requirements.txt
```

## Charts Generated

| Chart | Description |
|-------|-------------|
| `top_locations.png` | Cities with most job listings |
| `top_companies.png` | Companies hiring the most |
| `salary_mentions.png` | % of jobs that mention salary |
| `top_titles.png` | Most common job titles |

## Installation

```bash
git clone https://github.com/yourusername/job-scraper.git
cd job-scraper
pip install -r requirements.txt
```

## Usage

Run all steps with one command:

```bash
python main.py
```

Or run steps individually:

```bash
python scraper.py    # Step 1: Scrape
python cleaner.py    # Step 2: Clean
python analyzer.py   # Step 3: Analyze
```

## Tech Stack

- `requests` — HTTP requests
- `BeautifulSoup4` — HTML parsing
- `pandas` — Data cleaning
- `matplotlib` + `seaborn` — Visualization

## Author

Abdullah — Electronics & Computing Student
