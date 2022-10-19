# TwitterScraper

* Disclaimer: This is more of a personal practice rather than a serious scraper. If you're looking for a serious scraper, please find another one on github. However, if you're interested in the code, please feel free to read it or use it. Also, this scraper requires installation of selenium and chromedriver, it is stated in the requirement.txt file.

1. What's this for : It's a twitter scraper with proxy setting, for the purpose of downloading all the images from a particular twitter user page, then save the images to the local folder.

2. What is needed besides the py code files: all the libraries listed in the requirements.txt file, just follow the IDE's instruction to auto-install them. Also, the user needs to manully download a suitable chromedriver file and put it into the "driver" folder. Please leave the name as exactly as "chromedriver". Also, a Chrome browser is necessary.

3. How to use: 
- Run getHar.py, and input the twitter user link in the terminal or cmd. Then the Chrome itself will open the link and starts to scroll all the way down to load all the contents. 
- After it scrolls down to the very bottom, save the HAR file of the page (the dev tab will automatically open). Then save it as a txt file into the "HAR" folder.
- Now run twspider.py, input the name of the txt file you just saved in "HAR" folder. Then the scraper will start downloading all the images into the following path: ../Archive/[NameofTwitterUser]/. After downloads are finished, the scraper will say download finished and it can be terminated if needed.


*About the proxy setting: the proxy setting is in default on. If you don't need it, you can change the code in twspider.py to disable it. Please adjust accordingly to your own proxy setting in the proxy.txt file if you need the proxy. 

