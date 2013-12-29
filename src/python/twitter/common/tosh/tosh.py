import sqlparse

print sqlparse.parse('select * from foo;')

def run():
 while (1):
   x = raw_input('>')
   print "input is: " + x

def start():
  run()

start()
