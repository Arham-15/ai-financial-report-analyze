import pandas as pd
from extractor import extract_all_from_folder

def process_financials():
    records = extract_all_from_folder()

    df = pd.DataFrame(records)
    df.set_index("company", inplace=True)

    cols = ["revenue", "net_income", "total_assets", "total_liabilities", "cash_flow_operations"]
    for col in cols:
        df[col] = (df[col] / 1000).round(2)

    df.columns = ["Revenue (B)", "Net Income (B)", "Total Assets (B)", "Total Liabilities (B)", "Cash Flow Ops (B)"]

    df["Profit Margin (%)"] = ((df["Net Income (B)"] / df["Revenue (B)"]) * 100).round(2)
    df["Debt Ratio (%)"] = ((df["Total Liabilities (B)"] / df["Total Assets (B)"]) * 100).round(2)

    return df

if __name__ == "__main__":
    df = process_financials()
    print(df.to_string())