import sqlparse

class CommandParser:
  "Command parser for tosh."
  def parse(self, command):
    result = sqlparse.parse(command)
    stmt = result[0]
    return stmt.tokens

class TableOrientedShell:
  "Table Oriented shell (tosh) lets you access the system using a table oriented interface."
  def __init__(self):
    self.cmd_parser = CommandParser()

  def start(self):
    while (1):
      command = raw_input('>')
      print "input is: " + command
      print self.cmd_parser.parse(command)

tosh = TableOrientedShell()
tosh.start()