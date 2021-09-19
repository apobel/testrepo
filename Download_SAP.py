
import date, datetime

'''
Created on 24 Apr 2018

@author: a.belokas
'''

print('PAO')

# http://www.lagie.gr/fileadmin/user_upload/reports/DayAheadSchedulingResults/20180425_DayAheadSchedulingResults_01.xls

# Write a Downloader to download DAS results. 
# fromDate: the date we want to start downloading the data
# toDate: the date we want to end downloading the data


def downloadDAS():
        
    fromDate = datetime.date(2018, 4, 24)
    toDate = datetime.date(2018, 4, 25)
    
    # format Dates to use it in the link   
    fromDateText = str(year(fromDate)) + str(month(fromDate)) + str(day(fromDate))
     
    toDateText = str(year(toDate)) + str(month(toDate)) + str(day(toDate))
    
    print(fromDateText, toDateText) 
    
    
downloadDAS()
