#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from tracker.analyze import analyze_text
from tracker.viz import plot_daily_trend
from tracker.storage import fetch_entries, init_db

def main():
    print("== AI Mood Tracker MVP ==")
    init_db()
    while True:
        txt = input("\nEnter text (or 'q' to quit): ").strip()
        if txt.lower() in {"q", "quit", "exit"}:
            break
        if not txt:
            continue
        res = analyze_text(txt)
        print(f"→ label={res['label']} score={res['score']:.2f} meta={res['meta']}")
        img = plot_daily_trend()
        if img:
            print(f"✓ Trend plot updated: {img}")
        print("Recent entries:")
        for r in fetch_entries(limit=3):
            print(f"- [{r['ts']}] {r['sentiment']} ({r['score']:.2f}) :: {r['text'][:60]}")

if __name__ == '__main__':
    main()