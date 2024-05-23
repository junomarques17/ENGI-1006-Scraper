import pandas as pd


def readTables(url, diagnostic):
    tables = pd.read_html(url)
    
    #table diagnostic
    if diagnostic == True:
        print(f"Number of tables in url: {len(tables)}")
        #head() preview for every table
        for i, table in enumerate(tables):
            print(f"Info about table #{i+1}:\n{table.head()}\n")
        
    return tables
        
def scrapeTables(tables):
    """get #hw and #exams from tables"""
    num_hw = tables[0].shape[0]
    num_exams = tables[1].shape[0]

    return num_hw, num_exams