import os
from groq import Groq
from processor import process_financials
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def generate_summary():
    client = Groq(api_key=API_KEY)

    df = process_financials()

    data_text = ""
    for company in df.index:
        row = df.loc[company]
        data_text += f"""
{company}:
  - Revenue: ${row['Revenue (B)']}B
  - Net Income: ${row['Net Income (B)']}B
  - Total Assets: ${row['Total Assets (B)']}B
  - Total Liabilities: ${row['Total Liabilities (B)']}B
  - Cash Flow from Operations: ${row['Cash Flow Ops (B)']}B
  - Profit Margin: {row['Profit Margin (%)']}%
  - Debt Ratio: {row['Debt Ratio (%)']}%
"""

    prompt = f"""You are a professional financial analyst. Based on the following FY2025
financial data extracted from SEC 10-K filings, write a concise but insightful 200-word
summary comparing Tesla, Microsoft, and Apple. Highlight strengths, weaknesses, and key takeaways.

{data_text}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content

    print("===== AI GENERATED SUMMARY =====")
    print(summary)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("\nSummary saved to summary.txt")

    return summary

if __name__ == "__main__":
    generate_summary()