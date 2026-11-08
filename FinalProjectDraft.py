import requests
from bs4 import BeautifulSoup

response = requests.get('https://job-boards.greenhouse.io/pallet')
soup = BeautifulSoup(response.content, 'html.parser')
jobs = soup.find_all('tr', class_ = "job-post")

# Lisitis for role and location
jobsList = 'FinalProjectLists/jobTitlePython.csv'
locationList = 'FinalProjectLists/locationPython.csv'
roleAppendList = 'FinalProjectLists/approvedRoleList.csv'
roleAppendListNew = 'FinalProjectLists/approvedRoleListNew.csv'

jobListings = []

# Checking role keywords
def csvReadJob(title):
    with open(jobsList, 'r', encoding = 'utf8') as fileSourceJob:
        for line in fileSourceJob:
            keywordJob = line.strip().lower()
            if keywordJob in title.lower():
                roleMatch = True
                return roleMatch
    return False

# Checking location keywords
def csvReadLocation(location):
    with open(locationList, 'r', encoding = 'utf8') as fileSourceLocation:
        for line in fileSourceLocation:
            keywordLocation = line.strip().lower()
            if keywordLocation in location.lower():
                locationMatch = True
                return locationMatch
    return False

# Write new roles to cvs file & adding headers
# https://www.geeksforgeeks.org/python/how-to-add-a-header-to-a-csv-file-in-python/
def newRoleAppend(resultGTM):
    with open(roleAppendList, 'a', encoding = 'utf8') as fileSourceNewRole:
        fileSourceNewRole.write(resultGTM)
 
header = 'Role,Location,Link\n'
with open(roleAppendList, 'r', encoding = 'utf8') as fileSourceNewRole:
    content = fileSourceNewRole.read()
    
with open(roleAppendListNew, 'w', encoding = 'utf8') as fileSourceNewRoleNew:
    fileSourceNewRoleNew.write(header + content)
    

# Main
for job in jobs:
    jobItems = job.find_all('p')
    title = jobItems[0].get_text(strip = True)
    location = jobItems[1].get_text(strip = True)
    link = job.find('a').get('href')
    resultGTM = title + ',' + location + ',' + link + '\n'
    roleMatch = csvReadJob(title)
    locationMatch = csvReadLocation(location)
    if roleMatch and locationMatch:
        newRoleAppend(resultGTM)
        fileSourceNewRoleNew

        

       
