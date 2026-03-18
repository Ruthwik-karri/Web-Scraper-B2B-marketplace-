
# Web Scraping and Data Analysis Project

This repository contains a **Python-based web scraping project** that collects product data from IndiaMART for selected categories, saves it in structured formats, and performs **Exploratory Data Analysis (EDA)** and **data visualization**.

---

## Features

- Scrape product data from [IndiaMART](https://dir.indiamart.com/) using **Selenium** and **BeautifulSoup**.  
- Supports multiple product categories (`machinery`, `electronics`, `textiles`, etc.).  
- Saves scraped data in **JSON** and **CSV** formats.  
- Perform **EDA** to summarize data, check missing values, and analyze product distributions.  
- Generate **visualizations** of top products using **Matplotlib** and **Seaborn**.  
- Simple and modular code for easy customization and extension.  

---

## Project Structure
---bash
web-scraping-project/
│
├─ output/ # Folder containing JSON and CSV outputs
│ ├─ products.json
│ └─ products.csv
│
├─ main.py# Main script for scraping and analysis
└─ initial.py
|_README.md

---


---

## Installation

1. **Clone the repository**  

```bash
#git clone <your-repo-url>
#cd web-scraping-project

##depeneces
2.**Install dependencies**

pip install selenium beautifulsoup4 pandas matplotlib seaborn

3. Run the scraper

python main.py
