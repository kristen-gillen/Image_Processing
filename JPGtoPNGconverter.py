#need to be able to grab arguments and files

import sys
import os
import os.path
from PIL import Image

#grab the first and second argument 
image_folder = sys.argv[1]
print(image_folder)
new_folder = sys.argv[2]
print(new_folder)

#check if new folder exists, and if not create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
#loop through folder 

for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0] #returns tupple, grab first item for clean name
	img.save(f'{new_folder}{clean_name}.png','png')
#save to the new folder 