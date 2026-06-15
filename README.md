# 📊 AI Financial Report Analyzer

An automated financial analysis tool that extracts, processes, visualizes, and summarizes 
financial data directly from SEC 10-K PDF filings using Python and AI.

---

## 🚀 Features

- 📄 **Automatic PDF Extraction** — Extracts key metrics from any 10-K filing using `pdfplumber`
- 🧹 **Data Processing** — Cleans and structures data into a comparison DataFrame using `Pandas`
- 📈 **Visual Charts** — Generates 4 professional charts using `Matplotlib`
- 🤖 **AI-Generated Summary** — Produces analyst-style insights using `Groq (Llama 3.3 70B)`
- 📤 **Excel Export** — Exports everything into a formatted `.xlsx` report using `OpenPyXL`

---

## 🏢 Companies Analyzed (FY2025)

| Company   | Revenue   | Net Income | Profit Margin | Debt Ratio |
|-----------|-----------|------------|---------------|------------|
| Tesla     | $94.83B   | $3.79B     | 4.00%         | 39.87%     |
| Microsoft | $281.72B  | $101.83B   | 36.15%        | 44.51%     |
| Apple     | $416.16B  | $112.01B   | 26.92%        | 79.48%     |

---

## 🛠️ Tech Stack

| Tool         | Purpose                        |
|--------------|--------------------------------|
| pdfplumber   | PDF text extraction            |
| Pandas       | Data processing & analysis     |
| Matplotlib   | Chart generation               |
| Groq API     | AI summary (Llama 3.3 70B)     |
| OpenPyXL     | Excel report generation        |

---

## 📁 Project Structure
---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/Arham-15/ai-financial-report-analyzer.git
cd ai-financial-report-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
Open `ai_summary.py` and replace:
```python
API_KEY = "your-groq-api-key-here"
```

### 4. Add 10-K PDF files
Drop any SEC 10-K PDF files into the `pdfs/` folder.

### 5. Run the analyzer
```bash
python main.py
```

### 6. Get your report
Open `financial_report.xlsx` — contains metrics, ratios, charts, and AI summary.

---

## 📊 Sample Output

### Charts Generated
- Revenue Comparison
- Net Income Comparison  
- Cash Flow from Operations
- Profit Margin vs Debt Ratio

### Excel Report Sheets
- **Sheet 1** — Financial Metrics Table
- **Sheet 2** — Calculated Ratios
- **Sheet 3** — AI Generated Summary
- **Sheet 4** — Embedded Charts

---

## ⚠️ Notes

- Currently optimized for Tesla, Microsoft, and Apple 10-K filings
- Extensible to other companies by adding keyword mappings in `extractor.py`
- API key required for AI summary (free tier available at groq.com)

---

## 👨‍💻 Author

**Arham Hassan**  
B.Tech — AI & Data Science  
Integral University, Lucknow  

[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)](https://github.com/Arham-15)