import pandas as pd
import requests
import datetime as dt
# from bs4 import BeautifulSoup
pd.rea
# # Assign url of file: url
# url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# # Read in all sheets of Excel file: xls
# df = pd.read_excel(url, sheet_name=None)

# # Print the sheetnames to the shell
# print(*[key for key in df.keys()])

# # Print the head of the first sheet (using its name, NOT its index)
# pass


# url = 'https://www.wikipedia.org/'
# r = requests.get(url)

# r.headers.c

# if (r.status_code == requests.codes.not_found):
#     text = r.text
#     print(text)

today_date = dt.date.today()
print(today_date)