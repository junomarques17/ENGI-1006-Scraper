from library import (getPage, 
                     scrape, 
                     readTables,
                     scrapeTables,
                     formatOutput)

def main(url = 'https://www.cs.columbia.edu/~paine/1006/'):
    """Scraping the ENGI1006 course page."""
    #get relevant info from soup
    soup = getPage(url)
    soup_info = scrape(soup)
    
    #get relevant info from tables
    tables = readTables(url, diagnostic = False)
    pd_info = scrapeTables(tables)
    
    #combine data scraped from BeautifulSoup and pandas
    data = soup_info + pd_info
    
    #output function
    formatOutput(data)

if __name__ == '__main__':
    main()
