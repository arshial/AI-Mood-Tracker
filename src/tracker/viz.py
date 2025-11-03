import matplotlib.pyplot as plt

from .storage import fetch_daily_mean


def plot_daily_trend(out_path: str = "data/processed/daily_trend.png") -> str:
    stats = fetch_daily_mean()
    if not stats:
        return ""
    xs = [s["day"] for s in stats]
    ys = [s["mean_score"] for s in stats]
    plt.figure(figsize=(7, 3.2))
    plt.plot(xs, ys, marker="o")
    plt.title("Daily Mood Trend (mean score)")
    plt.xlabel("Day")
    plt.ylabel("Score [-1, 1]")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path