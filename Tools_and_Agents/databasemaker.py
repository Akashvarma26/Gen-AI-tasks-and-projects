# Importing the libraries to make db file
import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()

# Create table
table_info="""
create table STUDENT(NAME VARCHAR(25), SECTION VARCHAR(5), MARKS INT)
"""
cursor.execute(table_info)
# Insert values
cursor.execute("INSERT INTO STUDENT VALUES('Akash Varma','AIC',95)")
cursor.execute("INSERT INTO STUDENT VALUES('Aman Parasher','AIC',95)")
cursor.execute("INSERT INTO STUDENT VALUES('Sreyas Sai','AIC',95)")

# Show all data
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

conn.commit()
conn.close()