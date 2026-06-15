import matplotlib.pyplot as plt
import os
from processor import process_financials

def create_charts():
    df = process_financials()
    os.makedirs("charts", exist_ok=True)

    companies = df.index.tolist()
    colors = ["#E31937", "#00A4EF", "#555555"]  # Tesla red, Microsoft blue, Apple gray

    def save_chart(filename):
        plt.tight_layout()
        plt.savefig(f"charts/{filename}", dpi=150)
        plt.close()
        print(f"Saved: charts/{filename}")

    # Chart 1 — Revenue
    plt.figure(figsize=(8, 5))
    bars = plt.bar(companies, df["Revenue (B)"], color=colors)
    plt.title("Revenue Comparison (FY2025)", fontsize=14, fontweight="bold")
    plt.ylabel("USD Billions")
    plt.ylim(0, max(df["Revenue (B)"]) * 1.2)
    for bar, val in zip(bars, df["Revenue (B)"]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                 f"${val}B", ha="center", fontweight="bold")
    save_chart("revenue.png")

    # Chart 2 — Net Income
    plt.figure(figsize=(8, 5))
    bars = plt.bar(companies, df["Net Income (B)"], color=colors)
    plt.title("Net Income Comparison (FY2025)", fontsize=14, fontweight="bold")
    plt.ylabel("USD Billions")
    plt.ylim(0, max(df["Net Income (B)"]) * 1.2)
    for bar, val in zip(bars, df["Net Income (B)"]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f"${val}B", ha="center", fontweight="bold")
    save_chart("net_income.png")

    # Chart 3 — Cash Flow from Operations
    plt.figure(figsize=(8, 5))
    bars = plt.bar(companies, df["Cash Flow Ops (B)"], color=colors)
    plt.title("Cash Flow from Operations (FY2025)", fontsize=14, fontweight="bold")
    plt.ylabel("USD Billions")
    plt.ylim(0, max(df["Cash Flow Ops (B)"]) * 1.2)
    for bar, val in zip(bars, df["Cash Flow Ops (B)"]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f"${val}B", ha="center", fontweight="bold")
    save_chart("cash_flow.png")

    # Chart 4 — Profit Margin vs Debt Ratio
    x = range(len(companies))
    width = 0.35
    plt.figure(figsize=(9, 5))
    bars1 = plt.bar([i - width/2 for i in x], df["Profit Margin (%)"], width, label="Profit Margin (%)", color="#2ECC71")
    bars2 = plt.bar([i + width/2 for i in x], df["Debt Ratio (%)"], width, label="Debt Ratio (%)", color="#E74C3C")
    plt.title("Profit Margin vs Debt Ratio (FY2025)", fontsize=14, fontweight="bold")
    plt.ylabel("Percentage (%)")
    plt.xticks(list(x), companies)
    plt.legend()
    for bar in bars1:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{bar.get_height()}%", ha="center", fontsize=9)
    for bar in bars2:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{bar.get_height()}%", ha="center", fontsize=9)
    save_chart("margin_vs_debt.png")

    print("\nAll 4 charts saved in charts/ folder!")

if __name__ == "__main__":
    create_charts()