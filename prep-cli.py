import glob
import os
import sys

from PIL import Image
from tqdm import tqdm

img_list = list()
filtered_list = list()
#squares = list()

width_threshold, hight_threshold = int(sys.argv[1]), int(sys.argv[2])
heights, widths = 0, 0

# Collecting file paths:
for filepath in glob.glob(sys.argv[3]+'/**/*.jpg', recursive=True):
    img_list.append(filepath)

# Copying the paths of the images that pass the threshold into another list: 
for i in img_list:
    img = Image.open(i)
    if (img.size[0] >= hight_threshold) and (img.size[1] >= width_threshold):
        filtered_list.append(i)
        heights += img.size[0]
        widths += img.size[1]
        #if img.size[0] == img.size[1]:
            #squares.append(img)

# Calculating average height and width of all the accepted images:
avg_height = heights/len(filtered_list)
avg_width = widths/len(filtered_list)


print ("Total number of images in the source folder:", len(img_list), "images.")
print ("-----------------------")
print ("After filtering out images below "+ sys.argv[1]+"x"+sys.argv[2]+", "+str(len(filtered_list)), "images remain.")
print (len(img_list) - len(filtered_list), "images below threshold got discarded.")
#print (len(squares), " images have equal height and width.")
print ("-----------------------")

print ("Average height and width of the filtered images:", str(int(avg_height)) + "x" + str(int(avg_width)))
print ("Resizing the images that passed the dimension thresholds to the average dimensions...")



# cloning source folder and paths, and changing the name of the source folder into the output folder.
# keeping in mind not to clone any directories with no images that passed threshold.
# then creating new photos from the source with the new dimesnions.

for filepath in tqdm(glob.iglob(sys.argv[3]+"/**/*.jpg", recursive=True), ascii="░▒█", desc="Processing", total=len(img_list), colour="green"):
    if filepath in filtered_list:
        img = Image.open(filepath)
        new_image = img.resize((int(avg_height), int(avg_width)))
        output_filepath = filepath.replace(sys.argv[3], sys.argv[4])
        output_dir = os.path.dirname(output_filepath)
        os.makedirs(output_dir, exist_ok=True)
        img.save(output_filepath, 'JPEG')

print ("-----------------------")
print ("Saved the final set to "+sys.argv[4]+", preserving the original folder structure inside.")