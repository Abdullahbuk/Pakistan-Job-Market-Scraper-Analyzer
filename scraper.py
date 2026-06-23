import pandas as pd
import time
import random
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    """Set up Chrome in headless mode (no window opens)."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service, options=options)
    return driver


def scrape_jobs(keyword="python", location=None, pages=3):
    """
    Uses Selenium to scrape job listings from Rozee.pk.
    Returns a list of job dictionaries.
    """
    driver   = create_driver()
    all_jobs = []

    try:
        encoded_keyword  = quote_plus(keyword)
        encoded_location = quote_plus(location) if location else None

        for page in range(pages):
            start = page * 20
            if encoded_location:
                url = (
                    f"https://www.rozee.pk/job/jsearch/q/{encoded_keyword}/l/{encoded_location}/fpn/{start}"
                )
            else:
                url = f"https://www.rozee.pk/job/jsearch/q/{encoded_keyword}/fpn/{start}"

            print(f"Scraping page {page + 1}... ({url})")
            driver.get(url)

            # Wait until job cards appear
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.job"))
                )
            except Exception:
                print("  Page took too long or no jobs found.")
                break

            # Find all job cards
            job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job")

            if not job_cards:
                print("  No job cards found.")
                break

            for card in job_cards:
                title    = get_text(card, By.CSS_SELECTOR, "h3")
                company  = get_text(card, By.CSS_SELECTOR, "bdi a:first-child")
                location = get_text(card, By.CSS_SELECTOR, "bdi a:nth-child(2)")
                salary   = get_text(card, By.CSS_SELECTOR, "i.sal + span")

                # Skip empty/ad cards
                if not title:
                    continue

                all_jobs.append({
                    "title":    title    or "N/A",
                    "company":  company  or "N/A",
                    "location": location or "N/A",
                    "salary":   salary   or "N/A",
                })

            print(f"  Collected {len(all_jobs)} jobs so far.")
            time.sleep(random.uniform(2, 4))  # Polite delay

    finally:
        driver.quit()  # Always close browser

    print(f"\nTotal jobs scraped: {len(all_jobs)}")
    return all_jobs


def get_text(parent, by, selector):
    """Safely get text from an element. Returns None if not found."""
    try:
        element = parent.find_element(by, selector)
        return element.text.strip()
    except Exception:
        return None


def save_to_csv(jobs, filepath="data/raw_jobs.csv"):
    df = pd.DataFrame(jobs)
    df.to_csv(filepath, index=False)
    print(f"Saved to {filepath}")


if __name__ == "__main__":
    jobs = scrape_jobs(keyword="python", pages=3)
    if jobs:
        save_to_csv(jobs)