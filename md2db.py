#!/usr/bin/env python

import sqlite3

source = "mikro.md"
md = open(source)

result = []
date = ""
content = u""

# extract date and content and remove redundand new lines etc.
for line in md:
  if line[0:3] == "###":
    if date:
      date = date.strip()
      time_formatted = date[11:]
      day = date[0:2]
      month = date[3:5]
      year = '20' + date[6:8]
      date_formatted =  year + '-' + month + '-' + day + ' ' + time_formatted
      result.append((date_formatted, content.strip()))
      content = ""
    date = line[4:]
  else:
    content += line

md.close()

# save extracted data to database
result.reverse() # to make oldest entries have the lowest id in databse
conn = sqlite3.connect("mikro.db")
conn.text_factory = str
c = conn.cursor()
c.execute('''CREATE TABLE posts (date TEXT, content TEXT)''')

for post in result:
  c.execute('INSERT INTO posts (date, content) VALUES (?, ?)', post)

conn.commit()
conn.close()
