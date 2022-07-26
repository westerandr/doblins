import os

image_files = os.listdir("images/")

for image in image_files:
  image_doblins = image.split("doblins-")
  image_other_half = image_doblins[1].split(".png")
  number_id = int(image_other_half[0])
  old_filename = "images/" + image
  new_filename = "images/"+ str(number_id) +".png"
  os.rename(old_filename, new_filename)
  print("Successfully renamed " + old_filename + " to " + new_filename)
  
 