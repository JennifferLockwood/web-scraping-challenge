# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # Create mars_data dict that we can insert into mongoDB
    mars_data = {}

def latest_news():
    # Access and visit the NASA Mars News Site URL
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # HTML object
    html = browser.html

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain news title
    latest_news = soup.find_all('div', class_="list_text")

    # Get the latest news    
    news = latest_news[0]

    # Use BeautifulSoup' find() method to navigate and retrieve attributes
    news_title = news.find('div', class_="content_title")
    news_p = news.find('div', class_="article_teaser_body")