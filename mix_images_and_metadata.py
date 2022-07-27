import os
import json

def read_json_content(file_string):
  with open(file_string, 'r') as f:
    return json.load(f)

def replace_file_with_json_data(file_string, json_data):
  with open(file_string, 'w') as f:
    json.dump(json_data, f, indent=2)

# check if metadata folder is empty
if not os.listdir('metadata'):
  #exit 
  print('metadata folder is empty, please extract first')
  exit()
  
with open("json/3.json") as f:
  if "LEGENDARY" not in f.read():
    print("Already mixed")
    exit()

def mix(num_1, num_2):
  tmp_image = "images/tmp.png"

  first_metadata = "json/{}.json".format(num_1)
  first_image = "images/{}.png".format(num_1)

  second_metadata = "json/{}.json".format(num_2)
  second_image = "images/{}.png".format(num_2)


  #swap first and second metadata content
  first_metadata_content = read_json_content(first_metadata)
  second_metadata_content = read_json_content(second_metadata)
  tmp_metadata_content = second_metadata_content.copy()

  second_metadata_content["attributes"] = first_metadata_content["attributes"]
  first_metadata_content["attributes"] = tmp_metadata_content["attributes"]

  replace_file_with_json_data(first_metadata, first_metadata_content)
  replace_file_with_json_data(second_metadata, second_metadata_content)

  # swap #3 and #22 image filenames
  os.rename(first_image, tmp_image)
  os.rename(second_image, first_image)
  os.rename(tmp_image, second_image)
  
  print("Swapped #{} and #{}".format(num_1, num_2))


mix(3, 22)
mix(22, 85)
mix(16, 72)
mix(73, 103)
mix(30, 74)
mix(75, 110)
mix(25, 76)
mix(46, 109)

