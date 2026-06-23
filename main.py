"""
Pakistan Job Market Scraper & Analyzer
--------------------------------------
Run this file to:
1. Scrape job listings from Indeed
2. Clean the raw data
3. Generate analysis charts
"""

from scraper import scrape_jobs, save_to_csv
from cleaner import clean_jobs
from analyzer import run_analysis


def main():
    print("=" * 45)
    print("  Pakistan Job Market Scraper & Analyzer")
    print("=" * 45)

    # Step 1: Scrape
    print("\n[Step 1] Scraping job listings...")
    jobs = scrape_jobs(keyword="python developer", location="Pakistan", pages=3)

    if not jobs:
        print("No jobs found. Exiting.")
        return

    save_to_csv(jobs, filepath="data/raw_jobs.csv")

    # Step 2: Clean
    print("\n[Step 2] Cleaning data...")
    clean_jobs(
        input_path="data/raw_jobs.csv",
        output_path="data/clean_jobs.csv"
    )

    # Step 3: Analyze
    print("\n[Step 3] Generating charts...")
    run_analysis(path="data/clean_jobs.csv")

    print("\nDone! Check output/charts/ for your charts.")


if __name__ == "__main__":
    main()
