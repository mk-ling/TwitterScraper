import os
from selenium import webdriver

py_path = os.path.dirname(__file__)
path = os.path.join(py_path, 'driver', 'chromedriver')
url = input("Input URL ： ")
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
web = webdriver.Chrome(path, options=options)
web.get(url)

while True:
    web.execute_script("window.scrollTo(0, document.body.scrollHeight)")
