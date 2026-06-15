from extractor import extract_financials
from processor import process_financials
from visualizer import create_charts
from ai_summary import generate_summary
from exporter import export_to_excel

if __name__ == "__main__":
    print("Step 1/4 — Processing financial data...")
    process_financials()

    print("Step 2/4 — Creating charts...")
    create_charts()

    print("Step 3/4 — Generating AI summary...")
    generate_summary()

    print("Step 4/4 — Exporting to Excel...")
    export_to_excel()

    print("\nDone! Open financial_report.xlsx")