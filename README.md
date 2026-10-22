# python_scraper

A Python-based financial data scraping and browser automation toolkit designed to extract equity market metrics (such as 52-week high and low prices) from financial platforms including Moneycontrol and the National Stock Exchange of India (NSE).

---

## 📌 Overview

This project provides utilities for scraping both static and JavaScript-heavy financial web pages:
- **`app.py`**: Lightweight HTTP scraping using `requests` and `BeautifulSoup4` to fetch 52-week price extremes from Moneycontrol stock quote pages.
- **`pw_app.py`**: Headless browser automation using `playwright` with custom User-Agent configurations to extract equity price data from dynamic portals like NSE India.
- **`pw_example.py`**: A standalone sample script illustrating headless browser initialization and element extraction using Playwright.

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Dynamic Browser Automation:** [Playwright](https://playwright.dev/python/) (`playwright`)
- **HTTP Client:** [Requests](https://requests.readthedocs.io/) (`requests`, `urllib3`, `certifi`)
- **HTML Parsing:** [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) (`beautifulsoup4`, `soupsieve`)
- **Async & Concurrency Primitives:** `greenlet`, `pyee`

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.9+ installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/p8kaushal/python_scraper.git
cd python_scraper
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

For running scripts that utilize Playwright (`pw_app.py`, `pw_example.py`), install the required browser binaries:

```bash
playwright install chromium
```

---

## 💻 Usage

### 1. Scrape Moneycontrol (`app.py`)
Fetches 52-week high and low stock prices for a specified stock symbol (e.g., `RELIANCE`):

```bash
python app.py
```

### 2. Dynamic Scraping via Playwright (`pw_app.py`)
Launches a headless browser instance to retrieve stock metrics from NSE India:

```bash
python pw_app.py
```

### 3. Basic Playwright Test (`pw_example.py`)
Verifies the Playwright setup by launching a headless browser and reading page elements:

```bash
python pw_example.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
