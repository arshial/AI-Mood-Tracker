import matplotlib.pyplot as plt
from pathlib import Path

from .storage import fetch_daily_mean


def plot_daily_trend(out_path: str | Path = "data/processed/daily_trend.png") -> str:
    stats = fetch_daily_mean()
    if not stats:
        return ""

    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    xs = [s["day"] for s in stats]
    ys = [s["mean_score"] for s in stats]
    plt.figure(figsize=(7, 3.2))
    plt.plot(xs, ys, marker="o")
    plt.title("Daily Mood Trend (mean score)")
    plt.xlabel("Day")
    plt.ylabel("Score [-1, 1]")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(path, dpi=160)
    plt.close()
    return str(path)
