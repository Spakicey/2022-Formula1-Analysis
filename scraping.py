# ----------------------------------------
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
import os
# ----------------------------------------
# Initialize splinter and scraping
# ----------------------------------------
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Initialize empty dict for dict of DataFrames
    data = {}

    # Call function
    scrapeF1Tables(data, browser)

    # Stop browser and return data
    browser.quit()
    return data
# ----------------------------------------


# Scrape data
# ----------------------------------------
def scrapeF1Tables(data, browser):
    # Visit Formula 1 site
    url = 'https://www.formula1.com/en/results.html'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.resultsarchive-filter-wrap', wait_time=5)

    # Set up html parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.resultsarchive-filter-container')

    # Click accept cookies
    browser.find_by_id('truste-consent-button').click()

    # Get list of partial race links
    partial_link = slide_elem.findAll('a', class_='resultsarchive-filter-item-link FilterTrigger')
    race_partial_hrefs = [link.get('href') for link in partial_link[-22:-9]]

    # Print race hrefs
    for count, value in enumerate(race_partial_hrefs):
        print(f"Count: {count}")
        print(f"Value: {value}")


    # Function adapted to Python from http://darrellgrainger.blogspot.com/2012/06/staleelementexception.html
    def retryingFindClick(link):
        result = False
        attempts = 0
        while (attempts < 2):
            try:
                browser.links.find_by_partial_href(link).click()
                result = True
                break
            except StaleElementReferenceException:
                attempts += 1

        return result


    race_result_data = pd.DataFrame()
    side_col_data_df = pd.DataFrame()
    f1_url = 'https://www.formula1.com'
    os.makedirs('./data/', exist_ok=True)

    # Scrape data
    for count, race_href in enumerate(race_partial_hrefs):
        print(f"{count} iterate")
        print(f"race link | {race_href}")

        # Click link using partial
        retryingFindClick(race_href)

        # Get full race results link
        race_result_full_url = f'{f1_url}{race_href}'
        print(race_result_full_url)

        # Export race result table to CSV
        race_result_data = pd.read_html(race_result_full_url)[0]
        if (count > 9):
            # race_result_data.to_csv(f'./data/{count}_0_df.csv', index=False)
            data[f'{count}_0_df'] = race_result_data
        else:
            # race_result_data.to_csv(f'./data/0{count}_0_df.csv', index=False)
            data[f'0{count}_0_df'] = race_result_data

        # Delay for loading the page
        browser.is_element_present_by_css('a.side-nav-item-link ArchiveLink')

        # Get side column data
        # Set up new html parser and get partial link
        html = browser.html
        news_soup = soup(html, 'html.parser')
        slide_elem = news_soup.select_one('div.resultsarchive-wrapper')

        # Delay for loading the page
        browser.is_element_present_by_css('ul.resultsarchive-side-nav')

        side_col_data = slide_elem.findAll('a', class_='side-nav-item-link ArchiveLink')
        # Loop through side column data
        for i in range(len(side_col_data)):
            # Get URL to read table into DF
            side_col_data_partial_link = side_col_data[i].get('href')
            print(side_col_data_partial_link)
            side_col_data_full_url = f'{f1_url}{side_col_data_partial_link}'
            # Export side column tables to CSVs
            side_col_data_df = pd.read_html(side_col_data_full_url)[0]
            if (count > 9):
                # side_col_data_df.to_csv(f'./data/{count}_{i+1}_df.csv', index=False)
                data[f'{count}_{i+1}_df'] = side_col_data_df
            else:
                # side_col_data_df.to_csv(f'./data/0{count}_{i+1}_df.csv', index=False)
                data[f'0{count}_{i+1}_df'] = side_col_data_df

        # Reset html parser
        html = browser.html
        news_soup = soup(html, 'html.parser')
        slide_elem = news_soup.select_one('div.resultsarchive-filter-item-link FilterTrigger')
# ----------------------------------------

# Main method
# ----------------------------------------
if __name__ == "__main__":
  # If running as script, print scraped data
  print(scrape_all())

  # scrapeAll()
# ----------------------------------------

