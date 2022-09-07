# print("halo, saya mod.py")

import sys
# print(sys.argv)

# msg = ""
# while(msg != "stop"):
#   msg = input("isi pesan:")
#   print("pesan diterima:", msg)

print()

def makan(makanan):
  print("andi makan", makanan)
  
def minum(minuman):
  print("andi minum", minuman)

def listCommands(commands):
  for com in commands:
    print(com)

if (len(sys.argv) > 2):
  if (sys.argv[1] == "makan"):
    makan(sys.argv[2])
  elif (sys.argv[1] == "minum"):
    minum(sys.argv[2])
  else:
    listCommands(sys.argv)

print()
print("script stopped.")