import json, os, sys

def add_user(users, file_name):
  file = open(file_name, "r")
  jsonData = json.load(file)
  # print(jsonData)
  name = jsonData["profile"]["real_name_normalized"]
  users[jsonData["id"]] = name
  print("added:", name)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Include the directory which holds all the user json files and the directory which holds all the channels")
    print("i.e. python3 data-parse.py data/users/members data/channels")
    exit(0)
  dir_path = os.path.dirname(os.path.realpath(__file__))
  directory = dir_path + "/" + sys.argv[1]
  users = dict()
  for filename in os.listdir(directory):
    add_user(users, directory + "/" + filename)
