import sqlparse


class CommandParser:
  "Command parser for tosh."

  def parse(self, command):
    result = sqlparse.parse(command)
    stmt = result[0]
    return self.extractTableName(stmt.tokens)

  # TODO: make this more robust
  def extractTableName(self, tokens):
    from_idx = self.getFromPosition(tokens)
    table_name_token = tokens[from_idx + 1]
    return table_name_token.value

  def getFromPosition(self, tokens):
    idx = 0
    for token in tokens:
      idx = idx + 1
      if (token.is_keyword and token.value == 'from'):
        return idx
    return 0


class TableOrientedShell:
  "Table Oriented shell (tosh) lets you access the system using a table oriented interface."

  def __init__(self):
    self.cmd_parser = CommandParser()

  def start(self):
    while (1):
      command = raw_input('>')
      print "input is: " + command
      print "output is: " + self.cmd_parser.parse(command)


tosh = TableOrientedShell()
tosh.start()