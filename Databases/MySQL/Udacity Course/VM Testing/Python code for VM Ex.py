'''1st Exercise'''

# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "SELECT name, id FROM students;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print ("Row data:")
print (rows)

# And let's loop over it too:
print()
print ("Student names:")
for row in rows:
  print ("  ", row[0])

db.close()


#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

new_query = "SELECT name, id from students ORDER BY name ASC;"



'''2nd Exercise'''

# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
# 

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()





