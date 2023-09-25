from inputimeout import inputimeout, TimeoutOccurred


CLI_PROMPT_STR = "cli# "

cmd_list = {}


def cliAdd(name, func):
  cmd_list[name] = func



def cliMain():
  cliUpdate(input(CLI_PROMPT_STR))
  
def cliUpdate(data:str):
  args = data.split(' ')
  cmd = args[0].upper()

  if cmd == "HELP":
    cliPrintList()
  elif args[0] in cmd_list.keys():
    cliRunCmd(args[0], args[1:])

def cliRunCmd(cmd, args):
  print('')
  cmd_list[cmd](args)
  print('')

def cliRunStr(cli_str:str):
  cliUpdate(cli_str)

def cliKeepLoop():
  try:
    inputimeout('', timeout=0.001)
  except TimeoutOccurred:
    return True
  return False

def cliPrintList():
  print("\n---------- cmd list ---------")
  for cmd in cmd_list.keys():
    print(cmd.upper())
  print("-----------------------------\n")
