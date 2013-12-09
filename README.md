# STATS SCRAPING

This repo contains code to scrape player statistics from the achahockey.org web page. This is a proof of concept and being developed for use to minimize labor for data entry. 

## Dependencies

* [Python 2.7](http://www.python.org/getit/)
* [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)

## Running the Code

After cloning the repo you can scrape data as follows:
	
	$ scrapy crawl acha

## Saving the Results

Scrapy supports several standards for storing scraped data. In order to store them in JSON, CSV or XML execute the respective command:

	$ scrapy crawl acha -o items.json -t json
	$ scrapy crawl acha -o items.csv -t csv
	$ scrapy crawl acha -o items.xml -t xml

## Issues

For more information on how to use Scrapy please see the [Scrapy Reference](http://doc.scrapy.org/en/latest/index.html)


## Contributing

This is an open source project. Feel free to fork it and submit pull requests at will. 


