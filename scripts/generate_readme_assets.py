from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT_DIR = Path(__file__).resolve().parent.parent / "assets"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save_journey_diagram() -> None:
    fig, ax = plt.subplots(figsize=(14, 4.8), dpi=150)
    fig.patch.set_facecolor("#fbf9f4")
    ax.set_facecolor("#fffdf8")

    steps = [
        "fraud_detection_complete.ipynb\nBaseline hybrid setup",
        "fraudshield_v2.ipynb\nIndustry-grade rules + adversarial suite",
        "fraudshield_v3.ipynb\n10-class model + parallel ensemble",
        "Production artifacts\nSaved model + Drive backup",
    ]
    x = np.arange(len(steps))
    y = np.zeros_like(x, dtype=float)

    ax.plot(x, y, color="#005f73", linewidth=3, alpha=0.85)
    colors = ["#bb3e03", "#0a9396", "#ae2012", "#386641"]
    ax.scatter(x, y, s=700, c=colors, zorder=3)

    for i, text in enumerate(steps):
        ax.text(
            i,
            0.12,
            text,
            ha="center",
            va="bottom",
            fontsize=10,
            color="#222222",
            fontweight="semibold",
        )

    ax.set_title("FraudShield Evolution Timeline", fontsize=16, fontweight="bold", color="#1b4332")
    ax.set_ylim(-0.25, 0.45)
    ax.set_xlim(-0.4, len(steps) - 0.6)
    ax.axis("off")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "overview_pipeline.png", bbox_inches="tight")
    plt.close(fig)


def save_class_distribution() -> None:
    labels = [
        "benign",
        "impersonation",
        "kyc_scam",
        "phishing_link",
        "fake_payment_portal",
        "account_block_scam",
        "vishing",
        "delivery_scam",
        "social_engineering",
        "investment_scam",
    ]
    values = [3310, 1010, 930, 894, 726, 359, 40, 40, 40, 40]

    fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("#ffffff")

    bars = ax.bar(labels, values, color="#1d3557", edgecolor="#0b132b", alpha=0.95)
    ax.set_title("FraudShield v3 Final Training Distribution", fontsize=15, fontweight="bold")
    ax.set_ylabel("Samples")
    ax.grid(axis="y", linestyle="--", alpha=0.25)
    ax.tick_params(axis="x", rotation=35)

    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 20,
            str(val),
            ha="center",
            va="bottom",
            fontsize=8,
        )

    fig.tight_layout()
    fig.savefig(OUT_DIR / "final_class_distribution.png", bbox_inches="tight")
    plt.close(fig)


def save_metrics_chart() -> None:
    metrics = ["Accuracy", "F1 Macro", "F1 Weighted"]
    scores = [0.6078, 0.6126, 0.5810]

    fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=150)
    fig.patch.set_facecolor("#fff8f0")
    ax.set_facecolor("#fffdf9")

    bars = ax.bar(metrics, scores, color=["#023047", "#219ebc", "#8ecae6"], edgecolor="#1d3557")
    ax.set_ylim(0, 1.0)
    ax.set_title("Held-Out Test Metrics (Step 14)", fontsize=15, fontweight="bold")
    ax.set_ylabel("Score")
    ax.grid(axis="y", linestyle=":", alpha=0.35)

    for b, s in zip(bars, scores):
        ax.text(
            b.get_x() + b.get_width() / 2,
            s + 0.02,
            f"{s:.4f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    fig.tight_layout()
    fig.savefig(OUT_DIR / "final_metrics.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_journey_diagram()
    save_class_distribution()
    save_metrics_chart()
    print(f"Assets generated in: {OUT_DIR}")