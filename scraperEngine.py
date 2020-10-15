from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import urllib

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

class returnLinks:
    def __init__(self, url, name):
        self.url = url
        self.name = name

def getLinks(link, element):
    driver.get(link)

    list_of_hrefs = []

    content_blocks = driver.find_elements_by_class_name(element)

    for block in content_blocks:
        elements = block.find_elements_by_tag_name("a")
        for el in elements:
            list_of_hrefs.append(returnLinks(el.get_attribute("href"), el.get_attribute('innerHTML')))
            print('LINK FOUND: {}'.format(el.get_attribute("href")))
        
    f = open('output.json', 'w+')

    for index, x in enumerate(list_of_hrefs):
        try:
            f.write("{{ url: '{}', name: '{}' }},\n".format(x.url, x.name) )
        except:
            pass
    
    print('Save to output.json')
    f.close()