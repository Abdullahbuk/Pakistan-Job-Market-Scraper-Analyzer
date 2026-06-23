import pandas as pd


def clean_jobs(input_path="data/raw_jobs.csv", output_path="data/clean_jobs.csv"):
    """
    Cleans the raw jobs CSV:
    - Removes duplicates
    - Strips whitespace
    - Standardizes location names
    - Fills missing values
    """
    df = pd.read_csv(input_path)
    print(f"Rows before cleaning: {len(df)}")

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Strip whitespace from all string columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Replace 'N/A' strings with actual NaN
    df.replace("N/A", pd.NA, inplace=True)

    # Standardize common Pakistani city names
    city_map = {
        "karachi": "Karachi",
        "lahore":  "Lahore",
        "islamabad": "Islamabad",
        "rawalpindi": "Rawalpindi",
        "peshawar": "Peshawar",
        "quetta": "Quetta",
        "remote": "Remote",
    }

    def standardize_location(loc):
        if pd.isna(loc):
            return "Unknown"
        loc_lower = str(loc).lower()
        for key, value in city_map.items():
            if key in loc_lower:
                return value
        return str(loc).title()

    df["location"] = df["location"].apply(standardize_location)

    # Fill remaining NaN values
    df["title"]   = df["title"].fillna("Unknown Title")
    df["company"] = df["company"].fillna("Unknown Company")
    df["salary"]  = df["salary"].fillna("Not Mentioned")

    print(f"Rows after cleaning:  {len(df)}")
    df.to_csv(output_path, index=False)
    print(f"Saved clean data to {output_path}")

    return df


if __name__ == "__main__":
    clean_jobs()
