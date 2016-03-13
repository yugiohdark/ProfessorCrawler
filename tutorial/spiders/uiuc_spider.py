import scrapy
from tutorial.items import ProfessorItem
from selenium import webdriver
import time

class UIUCSpider(scrapy.Spider):
    name = "uiuc"
    start_urls = [
        "https://cs.illinois.edu/directory/faculty?quicktabs_faculty_tabs_new=0#quicktabs-faculty_tabs_new",
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        # use any browser you wish
        self.driver = webdriver.Firefox() 
    def __del__(self):
        self.driver.close()

    def parse(self, response):
        #start browser
        self.driver.get(response.url)
        #loading time interval
        time.sleep(5)
        # get the data and write it to scrapy items
        for sel in self.driver.find_elements_by_css_selector('#quicktabs_tabpage_faculty_tabs_new_0 .extDirectoryPerson'):
            item = ProfessorItem()
            item['name'] = sel.find_element_by_css_selector('.extDirectoryName a').text
            yield item
        self.driver.close()