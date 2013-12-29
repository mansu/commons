import sqlparse


class Command:
  "A tosh command."

  def __init__(self, command_type, command, arguments):
    self.command_type = command_type
    self.command = command
    self.arguments = arguments

  def __str__(self):
    return "Command type: %s, command: %s, arguments: %s" % \
           (self.command_type, self.command, self.arguments)

class CommandParser:
  "Command parser for tosh."

  def parse(self, command):
    result = sqlparse.parse(command)
    return self.getCommand(result[0].tokens)

  def getCommand(self, tokens):
    cmd_type = self.getCommandType(tokens[0])
    cmd = self.extractTableName(tokens)
    args = ''
    return Command(cmd_type, cmd, args)

  def getCommandType(self, token):
    if ((token.is_keyword) and (token.value == 'select' or token.is_keyword == 'describe')):
      return token.value
    return ''

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
      print "output is: " + str(self.cmd_parser.parse(command))


tosh = TableOrientedShell()
tosh.start()