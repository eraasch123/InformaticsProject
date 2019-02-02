import pandas as pd
import re


# read in the data to pandas dataframe ########################################################################
rates = pd.read_excel('Part 1.2 HW1.xlsx',
                       skiprows=2,                      # skip 1st 5 rows of excel file
                       header=[2],                   # header is now in the first and 2nd r                   # skip last 13 rows of excel file
                       index_col=0)             # index columns are 1st - 3rd in excel file but add total to
                                                                # keep it out of multiindex


new_DF = pd.melt(rates, id_vars=["State"], value_vars=['2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007'
                                                        ,'2006','2005','2004','2003','2002','2001','2000','1999','1995','1990'],
                                                        var_name="Year",
                                                        value_name="Rates").sort_values(by=["State","Year"])

new_DF.to_csv('/Users/Evan/Desktop/new_HW1_data.csv')