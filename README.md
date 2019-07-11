# Congress scraper

I wanted a historical list of who was in congress and when.  There were no CSVs that I could find so I wrote a quick scraper for https://www.congress.gov.  Running the program will produce a csv containing 
Congress number, member number, Chamber, Name (Last, First), State, and Party.

## Getting Started

This is a quick and dirty script.  Simply run python3 congress.py3 and the program will produce congress.csv in the output directory.
---
python3 ./congress.py3
---
You can alter the behavior of the program using the control variables

### Control variables
---
base_url='https://www.congress.gov/members?q={"congress":%s}&pageSize=250%s'  #Base url for later substitution
pages=['','&page=2','&page=3']                                                #Pages to collect:  I haven't needed more than three pages but I only pulled the congresses listed
congresses=[89,90,91,92,93,94,95,96,97,98,99]                                 #List of congresses to get data for:  Add or remove as needed
ignore={'State:','Party:'}                                                    #Do not process elements with these contents:  These words are simply ignored while parsing
remove={'District:','Served:'}                                                #Remove these headers and data from elements:  When these headers are encountered they and the data that follows is ignored
remove_append={'Representative':'House','Senator':'Senate'}                   #Rules for deriving house or senate from title:  Parses member "title" and determines "Chamber" column.
header=('Congress','Number','Chamber','Name','State','Party')                 #Fields output from processing:  Header for the csv file.
output_filename="./congress.csv"                                              #Output file for results: Desination for output
---

### Prerequisites

This code was developed on WSL running Ubuntu 16.04.  Here are the setup instructions to make this run.
```
apt-get update
sudo apt install python-pip  #Only needed if pip isn't installed
sudo apt-get install python3-bs4

```

### Installing

The easiest way to get this running is to retrieve it from git.

```
git clone https://github.com/acushon/congress.git
```
## Authors

* **Al Cushon** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
