import csv
import requests
from bs4 import BeautifulSoup

# Navigation variables
base_url='https://www.congress.gov/members?q={"congress":%s}&pageSize=250%s'  #Base url for later substitution
pages=['','&page=2','&page=3']                                                #Pages to collect
congresses=[89,90,91,92,93,94,95,96,97,98,99]                                 #List of congresses to get data for

#Control variables
ignore={'State:','Party:'}                                                    #Do not process elements with these contents
remove={'District:','Served:'}                                                #Remove these headers and data from elements
remove_append={'Representative':'House','Senator':'Senate'}                   #Rules for deriving house or senate from title
header=('Congress','Number','Chamber','Name','State','Party')                 #Fields output from processing
output_filename="./congress.csv"                                              #Output file for results
#counter_regex='\d*.'

members_array=[]
members_array.append(header)                                                  #Append the header to the output
for congress in congresses:                                                   #Process each congress in the list
  member_counter=0
  for page in pages:
    raw = requests.get(base_url % (congress,page)).content.decode("utf-8")    #Make a call for each page
    soup = BeautifulSoup(raw, 'html.parser')
    members = soup.find_all('li', {'class': 'compact'})
    for member in members:                                                    #Process each member on the page
      skip=False
      member_array=[]
      temp_array=(str(congress) + "\n" + member.text).splitlines()
      for item in temp_array:                                                 #Analyze each element of the array using parsing rules
        if item != '':                                                        #Skip empty elements
          if item in remove:                                                  #Remove elements on the remove list if present
            skip=True
            continue
          if item not in ignore:                                              #Ignore elements on the ignore list if present
            if not skip:
              temp=item.strip()
              for key in remove_append:                                       #Perform replacements on the remove append list
                if key in temp:
                  member_array.append(remove_append[key])
                  temp=temp.replace(key,'').strip()
              member_array.append(temp)                                       #Append the cleaned array to the individual member array
            else:
              skip=False
      if int(member_array[1].replace('.','')) > member_counter:               #Check that this member is unique/not processed
        members_array.append(member_array)                                    #Add the completed member array to the members array
        member_counter=int(member_array[1].replace('.',''))
      else:                                                                   #If this page is a duplicate then don't process it.
        print("Duplicate detected for congress %s.  Run proceeding..." % member_array[0])
        break

output_file=open(output_filename,'w')
writer=csv.writer(output_file)
writer.writerows(members_array)
