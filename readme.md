# Scraping Trending Topics from X Using Selenium Automation

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.x-brightgreen.svg)
![Flask](https://img.shields.io/badge/flask-2.3.2-green.svg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

This project uses Flask for the backend and Selenium to automate the scraping of trending topics from X. It utilizes ScraperAPI for IP rotation to avoid getting blocked. The collected data is stored in a MongoDB database for further analysis. This can be useful for market research, social media analysis, and trend forecasting.

## Features

- Automated scraping of trending topics from X.
- IP rotation using ScraperAPI to avoid detection and blocking.
- Data storage in MongoDB.
- Flask backend to handle requests and manage scraping.
- Configurable scraping intervals.
- Error handling and logging.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DibyaJyotiMahanta/Scraping-Trending-Topics-from-X-Using-Selenium-Automation.git
    cd Scraping-Trending-Topics-from-X-Using-Selenium-Automation
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install ChromeDriver (Ensure it matches your Chrome version):
    - Download it from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/)
    - Place the `chromedriver` executable in your PATH or in the project directory.

5. Set up your environment variables in a `.env` file:
    ```plaintext
    MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
    SCRAPER_API_KEY=your_scraper_api_key
    FLASK_APP=app.py
    FLASK_ENV=development
    ```

## Usage

1. Start the Flask server:
    ```bash
    flask run
    ```

2. Access the scraping endpoint to start scraping:
    ```bash
    http://127.0.0.1:5000/scrape
    ```

3. The scraped data will be stored in your MongoDB collection.

## Project Structure

```plaintext
Scraping-Trending-Topics-from-X-Using-Selenium-Automation/
│
├── chromedriver  # or chromedriver.exe on Windows
├── .env
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── scraper.py
└── templates/
    └── index.html
```

## Contributing

Contributions are welcome! Please create a new issue to discuss your ideas or submit a pull request.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a new pull request.

## Contact

For any inquiries or feedback, please contact [Dibya Jyoti Mahanta](mailto:your-email@example.com).
