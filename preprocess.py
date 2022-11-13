from PIL import Image
import glob
import os
from tqdm import tqdm

img_list = list()
filtered_list = list()
#squares = list()

width_threshold, hight_threshold = 800, 800
heights, widths = 0, 0

for filepath in glob.glob('Embroidery/**/*.jpg', recursive=True):
    #print(filepath)
    img_list.append(filepath)

for i in img_list:
    img = Image.open(i)
    #print(img.size)
    if (img.size[0] >= hight_threshold) and (img.size[1] >= width_threshold):
        filtered_list.append(i)
        heights += img.size[0]
        widths += img.size[1]
        #if img.size[0] == img.size[1]:
            #squares.append(img)


avg_height = heights/len(filtered_list)
avg_width = widths/len(filtered_list)
#print(avg_height, " ", avg_width)


print ("Total number of images:", len(img_list), "images.")
print ("-----------------------")
print ("After filtering out images below a height/width threshold of 800x800:", len(filtered_list), "images remain.")
print (len(img_list) - len(filtered_list), "images below threshold - discareded.")
#print (len(squares), " images have equal height and width.")
print ("-----------------------")

   
print ("Average height and width of the filtered photos:", int(avg_height), "x", int(avg_width))


print ("Resizing the photos that pass dimension thesholds into the average dimensions:")

for filepath in tqdm(glob.iglob("Embroidery/**/*.*", recursive=True), ascii=True, desc="Progess", total=len(img_list), colour="green"):
    if filepath in filtered_list:
        img = Image.open(filepath)
        new_image = img.resize((int(avg_height), int(avg_width)))
        output_filepath = filepath.replace("Embroidery", "Final")
        output_dir = os.path.dirname(output_filepath)
        os.makedirs(output_dir, exist_ok=True)
        img.save(output_filepath, 'JPEG')

print ("-----------------------")
print ("Saved the final set to the \"Final\" directory preserving the original folder structure.")