from sqlparse import sqlparse

def hello():
  print "Hello"

hello()
sqlparse.split('select * from foo; select * from bar;')

