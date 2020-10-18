# scpr-coding-challenge
southern california public radio coding challenge



### Setup:

download the mongo DB daily dump for 2019-06-30 from here: `https://ghtorrent.org/downloads.html`

... this might take a few hours ...

install mongo DB if its not already installed with the command: `sudo apt-get install mongodb`

enter the mongo DB shell with the command: `mongo`

create a mongo DB database called "scpr_db" with the command: `use scpr_db`

exit the mongo DB shell with the command: `exit`

restore the downloaded daily dump with the command: `mongorestore -d scpr_db <path/to/dump/files>`

install the python libraries in requirements.txt with if not already installed: `pip3 install src/requirements.txt`

requirements.txt contains:
```
pymongo
requests
```


### Usage:

Run the following python scripts and the Solutions will be printed to the terminal:
```
python3 src/part1_bullet1.py
python3 src/part1_bullet2.py
python3 src/part1_bullet3.py
python3 src/part2_bullet1.py
python3 src/part2_bullet2.py
```

Each script takes 2-3 minutes to run, and the output should match the solutions in solutions.md. See the Data_Engineer_Assessment.docx file for the orginal questions.


