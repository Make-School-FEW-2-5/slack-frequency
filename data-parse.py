import json
import sys
import os
import re


def add_user(users, file_name):
    file = open(file_name, "r")
    jsonData = json.load(file)
    # print(jsonData)
    name = jsonData["profile"]["real_name_normalized"]
    users[jsonData["id"]] = name
    users[name] = jsonData["id"]
    print("added:", name)


def consolidate_messages(messages, channel_name, file_name, users):
    file = open(file_name, "r")
    jsonData = json.load(file)
    channelMessages = ""
    for entry in jsonData:
        message = entry["text"]
        m = re.search("([A-Z0-9]){9}", message)
        while m:
            if m.string[m.start():m.end()] not in users:
                m = re.search("([A-Z0-9]){9}", message)
                break
            message = m.string[:m.start()] + users[m.string[m.start():m.end()]] + m.string[m.end():]
            m = re.search("([A-Z0-9]){9}", message)
        channelMessages += message
    messages['channels'].append(
        {
            'channel': channel_name,
            'text': channelMessages
        }
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Include the directory which holds all the user json files and the directory which holds all the channels")
        print("i.e. python3 data-parse.py data/users/members data/channels")
        exit(0)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    user_directory = dir_path + "/" + sys.argv[1]
    users = dict()
    messages = {'channels': []}
    for filename in os.listdir(user_directory):
        add_user(users, user_directory + "/" + filename)

    for root, dir, files in os.walk(sys.argv[2]):
        for name in files:
            if name != ".gitkeep":
                consolidate_messages(
                    messages,
                    name[:-5],
                    os.path.join(dir_path, root, name),
                    users)
        print(name[:-5])
  
    with open('data.json', 'w') as outfile:
        json.dump(messages, outfile, indent=4)
