
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
  cmd_list[cmd](args)

def cliKeepLoop():
  input()

def cliPrintList():
  print("\n---------- cmd list ---------")
  for cmd in cmd_list.keys():
    print(cmd.upper())
  print("-----------------------------\n")