#import libraries

import pandas as pd

def scrape_fda_debarment_list(fda_website: str = None):
    # specify the URL of the FDA debarment list
    # easily changed if necessary
    fda_debarment_website = fda_website if fda_website else 'https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/fda-debarment-list-drug-product-applications'

    # read the HTML tables on the page into a list of DataFrames
    # there are two tables at the time of this publishing
    all_tables = pd.read_html(fda_debarment_website)

    # get the second table
    persons_table = all_tables[1]

    # remove the rows that do not have names
    persons_table = persons_table[persons_table['Last Name'].notna()]

    # save the table to a CSV file
    persons_table.to_csv('fda_debarment_list.csv', index=False)
