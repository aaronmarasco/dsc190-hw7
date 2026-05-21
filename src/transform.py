"""Stage 2: Add date column."""
import pandas as pd
from pathlib import Path

INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main():
    df = pd.read_csv(INPUT)
    # timestamps are ISO 8601, so the first 10 chars are the date
    df["date"] = df["timestamp"].str[:10]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()