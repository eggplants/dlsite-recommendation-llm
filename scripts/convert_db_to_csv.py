import csv
import sqlite3
import sys
from pathlib import Path

if __name__ == "__main__":
    conn = sqlite3.connect(sys.argv[1])
    c = conn.cursor()
    header = [
        "work.work_id",
        "title",
        "circle",
        "category",
        "sale_date",
        "description",
        "price",
        "series",
        "sales",
        "favorites",
        "rating",
    ]
    rows = c.execute(
        f"""
      SELECT {", ".join(header)}
      FROM work INNER JOIN option ON work.work_id = option.work_id
      WHERE rating IS NOT NULL AND sales >= 1000
      """,  # noqa: S608
    )

    header.pop()
    header.insert(0, "work_id")

    with Path(sys.argv[2]).open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    conn.close()
