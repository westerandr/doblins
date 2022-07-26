import os
import json

metadata_files = os.listdir("metadata/")

all_metadata = []

for data in metadata_files:
  if(data == "_metadata.json"):
    continue
  with open("metadata/"+data, "r") as f:
    json_data = json.loads(f.read())
    # print(type(json_data))
    
    all_metadata.append(json_data)
    
# sort json

  

with open("metadata/_metadata.json", "w") as mega_file:
  json.dump(all_metadata, mega_file, indent=2)
  print("Done creating _metadata.json file")

