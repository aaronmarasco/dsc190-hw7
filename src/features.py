"""Stage 3: Add duration_minutes and weekday columns."""
import pandas as pd
from pathlib import Path

INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")


def main():
    df = pd.read_csv(INPUT)
    df["duration_minutes"] = df["duration_seconds"] / 60
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()