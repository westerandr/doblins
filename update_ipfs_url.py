import sys
import os
import json

if sys.argv[1] == None:
  print("Please provide a CID as an argument")
  exit()

CID = sys.argv[1]

metadata_files = os.listdir("json/")

# loop through all the files in the directory and update the ipfs url
for data in metadata_files:
  if(data == "_metadata.json"):
    continue
  with open("json/"+data, "r") as f:
    num = int(data.split(".")[0])
    json_data = json.loads(f.read())
    # print(type(json_data))

    # replace placeholder text
    json_data["image"] = "ipfs://" + CID + "/" + str(num) + ".png"
    
  # write to file
  with open("json/"+data, "w") as f:
    json.dump(json_data, f, indent=2)
    print("Updated " + data)    
    
     