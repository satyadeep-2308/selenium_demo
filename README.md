# Selenium Amazon Scraper Demo

A simple Selenium automation project built for the MADSC301 — Business Intelligence Midterm Presentation.

This project demonstrates how Selenium can automate browser actions and collect real-time web data from JavaScript-heavy websites like Amazon.

---

# Project Objective

The purpose of this project is to demonstrate:

- Browser automation using Selenium
- Dynamic web scraping
- Automated product search
- Real-world Business Intelligence (BI) data collection

This demo simulates how businesses collect competitor pricing and product data for analytics dashboards and decision-making systems.

---

# Technologies Used

- Python 3
- Selenium WebDriver
- Google Chrome
- ChromeDriver (managed automatically by Selenium)

---

# Features

- Opens Amazon automatically
- Searches for a product
- Extracts product titles
- Extracts product prices
- Displays scraped data in terminal

---

# Project Structure

```text
.
├── amazon_selenium_demo.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/selenium-amazon-demo.git
cd selenium-amazon-demo
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the script using:

```bash
python amazon_selenium_demo.py
```

---

# Sample Workflow

1. Selenium launches Chrome browser
2. Opens Amazon website
3. Searches for "laptop"
4. Scrapes product titles and prices
5. Prints extracted data

---

# Example Output

```text
--- AMAZON PRODUCT DATA ---

1. Product: HP Laptop 15s
   Price: ₹52,990

2. Product: Lenovo IdeaPad Slim 3
   Price: ₹44,999
```

---

# Business Intelligence Use Case

Organizations use Selenium for:

- Competitor price monitoring
- Product trend analysis
- Market research
- Review collection
- Real-time data pipelines

The scraped data can later be stored in:

- CSV files
- Databases
- Data warehouses
- Power BI dashboards

---

# Important Notes

- Amazon may occasionally block automated scraping
- Website structure may change over time
- Selenium is slower than HTTP-based scraping because it runs a real browser

---

# Ethical Considerations

This project is created strictly for educational purposes.

Always:
- Respect robots.txt policies
- Avoid excessive requests
- Follow website terms of service

---

# References

1. Selenium Documentation  
https://www.selenium.dev/documentation/

2. Scrapy Documentation  
https://scrapy.org

3. Web Scraping with Python — Ryan Mitchell

---

# Author

Satyadeep Panga  
MADSC301 — Business Intelligence  
EU Business School
