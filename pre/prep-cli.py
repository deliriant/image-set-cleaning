import glob
import os
import sys

from PIL import Image
from tqdm import tqdm


png_list = list()
jpg_list = list()
jpeg_list = list()

img_list = list()
filtered_list = list()
#squares = list()

width_threshold, hight_threshold = int(sys.argv[1]), int(sys.argv[2])
heights, widths = 0, 0

# Collecting *.png paths:
for filepath in glob.glob(sys.argv[3]+'/**/*.png', recursive=True):
    png_list.append(filepath)
    img_list.append(filepath)

# Collecting *.jpg paths:
for filepath in glob.glob(sys.argv[3]+'/**/*.jpg', recursive=True):
    jpg_list.append(filepath)
    img_list.append(filepath)

# Collecting *.png paths:
for filepath in glob.glob(sys.argv[3]+'/**/*.jpeg', recursive=True):
    jpeg_list.append(filepath)
    img_list.append(filepath)


print ("Found", len(png_list), "png,", len(jpg_list), "jpg and", len(jpeg_list), "jpeg images.")



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

for filepath in tqdm(filtered_list, ascii="?????????", desc="Processing", total=len(filtered_list), colour="green"):
    img = Image.open(filepath)
    new_image = img.resize((int(avg_height), int(avg_width)))
    output_filepath = filepath.replace(sys.argv[3], sys.argv[4])
    output_dir = os.path.dirname(output_filepath)
    os.makedirs(output_dir, exist_ok=True)
    img.save(output_filepath, 'JPEG')

print ("-----------------------")
print ("Saved the finalized imageset to ./"+sys.argv[4]+"/, preserving the original folder structure inside.")
print ("Done!")