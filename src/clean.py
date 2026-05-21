"""Stage 1: Clean raw events data."""
import pandas as pd
from pathlib import Path

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")
VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}


def main():
    df = pd.read_csv(INPUT)

    # Drop rows with any missing fields
    df = df.dropna()

    # Coerce duration_seconds to numeric and drop unparseable
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])

    # Drop rows with non-positive duration
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Normalize timestamps to ISO 8601: YYYY-MM-DDTHH:MM:SS
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")
    df = df.dropna(subset=["timestamp"])
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()