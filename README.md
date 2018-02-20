# Coursera Dump

**A script that parses the coursera.org courses info and writes it to the Excel spreadsheet**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt
```
# Quickstart
**Ways to use:**
- Have to use  module `coursera.py` after `python3`.
 - You get info about 5 courses in courses_info.xmls by default.

Example of script launch on Linux, Python 3.5:


```bash
$ python3 coursera.py 
course(Course_name='Gamification', Grade='0 stars', Language='English', Start_date='Starts Feb 26', Amount_week='6 weeks')
course(Course_name='Dealing With Missing Data', Grade='3.9 stars', Language='English', Start_date='Started Feb 19', Amount_week='4 weeks')
course(Course_name='Vital Signs: Understanding What the Body Is Telling Us', Grade='0 stars', Language='English', Start_date='Started Feb 19', Amount_week='6 weeks')
course(Course_name='Modern Art & Ideas', Grade='4.6 stars', Language='English', Start_date='Started Feb 19', Amount_week='5 weeks')
course(Course_name='The Evolving Universe', Grade='4.6 stars', Language='English', Start_date='Starts Mar 12', Amount_week='5 weeks')
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
