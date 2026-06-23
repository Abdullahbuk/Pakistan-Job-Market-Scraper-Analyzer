import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use("Agg")  # Non-interactive backend for saving files

OUTPUT_DIR = "output/charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path="data/clean_jobs.csv"):
    return pd.read_csv(path)


def plot_top_locations(df):
    """Bar chart of top job locations."""
    counts = df["location"].value_counts().head(8)

    plt.figure(figsize=(10, 5))
    counts.plot(kind="bar", color="steelblue", edgecolor="white")
    plt.title("Top Job Locations", fontsize=14, fontweight="bold")
    plt.xlabel("City")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_locations.png", dpi=150)
    plt.close()
    print("Saved: top_locations.png")


def plot_top_companies(df):
    """Horizontal bar chart of companies with most listings."""
    counts = df["company"].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    counts.sort_values().plot(kind="barh", color="coral", edgecolor="white")
    plt.title("Top Hiring Companies", fontsize=14, fontweight="bold")
    plt.xlabel("Number of Job Listings")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_companies.png", dpi=150)
    plt.close()
    print("Saved: top_companies.png")


def plot_salary_mentions(df):
    """Pie chart showing how many jobs mention salary."""
    has_salary    = (df["salary"] != "Not Mentioned").sum()
    no_salary     = (df["salary"] == "Not Mentioned").sum()

    labels = ["Salary Mentioned", "Not Mentioned"]
    sizes  = [has_salary, no_salary]
    colors = ["#4CAF50", "#FF7043"]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("Jobs Mentioning Salary", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/salary_mentions.png", dpi=150)
    plt.close()
    print("Saved: salary_mentions.png")


def plot_top_job_titles(df):
    """Bar chart of most common job titles (cleaned)."""
    # Extract first 3 words from each title for grouping
    df["short_title"] = df["title"].apply(
        lambda t: " ".join(str(t).split()[:3])
    )
    counts = df["short_title"].value_counts().head(8)

    plt.figure(figsize=(10, 5))
    counts.plot(kind="bar", color="mediumpurple", edgecolor="white")
    plt.title("Most Common Job Titles", fontsize=14, fontweight="bold")
    plt.xlabel("Job Title")
    plt.ylabel("Count")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_titles.png", dpi=150)
    plt.close()
    print("Saved: top_titles.png")


def run_analysis(path="data/clean_jobs.csv"):
    df = load_data(path)
    print(f"\nAnalyzing {len(df)} job listings...\n")

    plot_top_locations(df)
    plot_top_companies(df)
    plot_salary_mentions(df)
    plot_top_job_titles(df)

    print("\nAll charts saved to output/charts/")


if __name__ == "__main__":
    run_analysis()
