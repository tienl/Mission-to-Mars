#!/usr/bin/env python
# coding: utf-8
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as Soup
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)
    title1, img_url1, thumb_url1 =  hemi_image1(browser)
    title2, img_url2, thumb_url2 =  hemi_image2(browser)
    title3, img_url3, thumb_url3 =  hemi_image3(browser)
    title4, img_url4, thumb_url4 =  hemi_image4(browser)

    # Run all scraping functions and store results in dictionary
    data = {
          "news_title": news_title,
          "news_paragraph": news_paragraph,
          "featured_image": featured_image(browser),
          "facts": mars_facts(),
          "thumb1": thumb_url1,
          "thumb2": thumb_url2,
          "thumb3": thumb_url3,
          "thumb4": thumb_url4,
          "title1": title1,
          "title2": title2,
          "title3": title3,
          "title4": title4,
          "img_url1": img_url1,
          "img_url2": img_url2,
          "img_url3": img_url3,
          "img_url4": img_url4,
          "last_modified": dt.datetime.now()
    }

    #stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = Soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# ## JPL Space Images Featured Image

def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

def hemi_image1(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find cerberus hemisphere enhanced and click that
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    hemi_elem = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    hemi_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')

    try:
        # Find the title and relative image url
        title = img_soup.find("h2", class_="title").get_text()
        thumb_url_rel = img_soup.find("img", class_="thumb").get("src")
        img_url_rel = img_soup.find("img", class_="wide-image").get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL, also prepare for return
    img_url1 = f'https://astrogeology.usgs.gov/{img_url_rel}'
    thumb_url1= f'https://astrogeology.usgs.gov/{thumb_url_rel}'
    title1=title

    return title1, img_url1, thumb_url1
def hemi_image2(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find cerberus hemisphere enhanced and click that
    browser.is_element_present_by_text('Schiaparelli Hemisphere Enhanced', wait_time=1)
    hemi_elem = browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced')
    hemi_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')

    try:
        # Find the title and relative image url
        title = img_soup.find("h2", class_="title").get_text()
        thumb_url_rel = img_soup.find("img", class_="thumb").get("src")
        img_url_rel = img_soup.find("img", class_="wide-image").get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url2 = f'https://astrogeology.usgs.gov/{img_url_rel}'
    thumb_url2 = f'https://astrogeology.usgs.gov/{thumb_url_rel}'
    title2 = title

    return title2, img_url2, thumb_url2
def hemi_image3(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find cerberus hemisphere enhanced and click that
    browser.is_element_present_by_text('Syrtis Major Hemisphere Enhanced', wait_time=1)
    hemi_elem = browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced')
    hemi_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')

    try:
        # Find the title and relative image url
        title = img_soup.find("h2", class_="title").get_text()
        thumb_url_rel = img_soup.find("img", class_="thumb").get("src")
        img_url_rel = img_soup.find("img", class_="wide-image").get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url3 = f'https://astrogeology.usgs.gov/{img_url_rel}'
    thumb_url3 = f'https://astrogeology.usgs.gov/{thumb_url_rel}'
    title3 = title

    return title3, img_url3, thumb_url3
def hemi_image4(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Find cerberus hemisphere enhanced and click that
    browser.is_element_present_by_text('Valles Marineris Hemisphere Enhanced', wait_time=1)
    hemi_elem = browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced')
    hemi_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')

    try:
        # Find the title and relative image url
        title = img_soup.find("h2", class_="title").get_text()
        thumb_url_rel = img_soup.find("img", class_="thumb").get("src")
        img_url_rel = img_soup.find("img", class_="wide-image").get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url4 = f'https://astrogeology.usgs.gov/{img_url_rel}'
    thumb_url4 = f'https://astrogeology.usgs.gov/{thumb_url_rel}'
    title4 = title

    return title4, img_url4, thumb_url4

def mars_facts():
    # ## Mars Facts
    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Value']
    df.set_index('Description', inplace=True)

    # Convert the table to html
    html_table = df.to_html()

    # Replace automatic strings in order to format the table in index.html
    html_table = html_table.replace('\n', '').replace('<th></th>      <th>Value</th>', '<th>Description</th> <th>Value</th>')
    html_table = html_table.replace('<th>Description</th>      <th></th>', ' ')
    html_table = html_table.replace('<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">', ' ')


    return html_table



if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
