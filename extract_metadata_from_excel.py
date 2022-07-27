import pandas as pd
import json

data = pd.read_excel('DOBLINS_TRAITS.xlsx')

LEGENDARY = "LEGENDARY"
GREEN_GOBLIN = "GREEN GOBLIN"
BALLOON = "BALLOON"
PINK_LADY = "PINK LADY"


for index, row in data.iterrows():
    bg = row[1]

    
    if bg in [LEGENDARY, GREEN_GOBLIN, BALLOON, PINK_LADY]:
      attributes = [ {"trait_type": "ONE OF ONES", "value": bg},]
    else:
      face = row[2]
      clothing = row[3]
      hat = row[4]
      hair = row[5]
      accessories = row[6]
      
  
      attributes = [
        {"trait_type": "BG", "value": bg},
        {"trait_type": "FACE", "value": face},
        {"trait_type": "CLOTHING", "value": clothing}
      ]

      
      if isinstance(hat, float):
        hat_value = "NONE"
      else:
        hat_value = hat
        
      if isinstance(hair, float):
        hair_value = "NONE"
      else:
        hair_value = hair
        
      if isinstance(accessories, float):
        accessories_value = "NONE"
      else:
        accessories_value = accessories
      
      attributes.extend([{"trait_type": "HAT", "value": hat_value},{"trait_type": "HAIR", "value": hair_value},{"trait_type": "ACCESSORIES", "value": accessories_value}])
      
    num_id = row[0]
    
    metadata = {
      "name": "Doblins #"+str(num_id),
      "description": "Doblins is a limited 111 PFP collection nesting on the Ethereum network.",
      "image": "ipfs://IPFS_URL/{}.png".format(num_id),
      "attributes": attributes
      }
      
    
    json_filename = str(num_id) + ".json" 
    with open("json/"+json_filename, 'w') as j:
      json.dump(metadata, j, indent=2)
    print(num_id, metadata)
    
    