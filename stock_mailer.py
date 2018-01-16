import time
import datetime
import random

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.keys import Keys

#Partial url of the website from which to scrape.
#The ticker symbol of a target stock can be concatenated to the end of nasdaq_symbol_url to form the url of its page.
global nasdaq_symbol_url
nasdaq_symbol_url = "https://www.nasdaq.com/symbol/"

def retrieve_stock_price(browser, ticker_symbol):
    '''Web scrapes the price of a particular stock.'''
    browser.get(nasdaq_symbol_url + ticker_symbol)
    price = browser.find_element_by_xpath('//div[@id="qwidget_lastsale"]').text
    return price

def collect_prices(browser, desired_symbols):
    '''Iterates through the list of symbols of the desired stocks, web scraping the price of each.  Returns a list
    of the results.'''
    prices_list = []
    for ticker_symbol in desired_symbols:
        prices_list.append((ticker_symbol, retrieve_stock_price(browser, ticker_symbol)))

    return prices_list


def write_email(prices_list):
    '''Formats the collected prices into a string, which will be the email body.'''
    email_body = ""
    for symbol_price_pair in prices_list:
        email_body = email_body + "\n" + symbol_price_pair[0] + ": " + symbol_price_pair[1]

    return email_body

def send_email(email_body, email_properties):
    '''Sends the email with collected stock prices.'''
    #Replace with your preferred email method.
    print email_body
    print "Email sent!"


stock_browser = webdriver.Chrome()

#Replace with the ticker symbols you're interested in.
desired_symbols = ['GOOG', 'AAPL', 'MSFT']

prices_list = collect_prices(stock_browser, desired_symbols)
email_body = write_email(prices_list)
send_email(email_body, "properties")


