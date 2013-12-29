import sqlparse

print sqlparse.parse('select * from foo;')

class ToShell:
    def start(self):
      while (1):
        x = raw_input('>')
        print "input is: " + x

tosh = ToShell()
tosh.start()
