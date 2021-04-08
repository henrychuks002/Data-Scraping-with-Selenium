# Data-Scraping-with-Selenium
Automating data collection via web scraping. How I collected jumia data on some of the available samsung devices on their online store with a bot using selenium

First off incase you haven't heard of selenium, because most programmers or data scientists I know often prefer to use the beautiful soup python library for their scraping projects,The python Selenium package like the beautiful soup is used to automate web browser interaction from python. Several browsers or drivers such as firefox and internet explorer are supported as well as the remote, For this project, the chrome web driver is utilized.
## Why Selenium?
Other than the fact that its easy to understand and code, some websites renders their content with the javascript, which means a simple get request to the page url would return only the visible content
## The Methodology
* Scraping the intented data from the website, For this, a good knowledge of XPATH and other selenium element locators would be very helpful
* After the scraping is done, then conversion or compilation of the scraped data into a single excel xlsx file and then lastly
* Sending the file as an attachment to a recipient email address, just incase one may be working in a team or in a collaboration 
The approach it takes is basically clicking on every device on the first five pages of the website after the "samsung phones" search is sent via the search box, next is getting the name of each device it clicks on, the prices of it and the star ratings, and then appending them  on separate lists and finally zipping them together in one list to create the excel file, and then lastly sending the file as an attachment to a recipient email address with python
For more details of the project check out the article I've published on it #link
porfolio at #link

One more thing worth noting is, In the jumiadata.py file, lines from 92 to 149 would actually be a good part to implement the python loop, for loop to be precise, which I have also written in a seperate file, it was only done this way given the few number of pages to be scraped, however if there were about a tens
of a bigger amount of pages to be scraped then the for loop which I ve also written as part this repo as "the for loop.py" should definitely
be implemented otherwise

The "the for loop.py" script is an associate of the jumiadata.py script just to show how else the entire line 92 to 149 of the jumiadata.py script could have been written. In essence, the entire lines 92 to 149 in the jumiadata.py can be comfortably replaced with lines 33 to 44 on the "the for loop.py".
