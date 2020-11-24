# To get list automatically from https://www.slickcharts.com/sp500

from selenium import webdriver
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def gettable():
    url = 'https://www.slickcharts.com/sp500'
    options = webdriver.ChromeOptions()
    # options.add_argument('--load-extension=enable')
    options.add_argument('--headless')
    # options.add_experimental_option("prefs", {
    #     "download.default_directory": ROOT_DIR,
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True
    # })

    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)
    table = driver.find_element_by_tag_name('table')
    return(table.text)

if __name__ == "__main__":
    gettable()
