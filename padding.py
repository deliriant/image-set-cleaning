from PIL import Image, ImageOps
import os


def padding(img, expected_size):
    desired_size = expected_size
    delta_width = desired_size - img.size[0]
    delta_height = desired_size - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding)


def resize_with_padding(img, expected_size):
    img.thumbnail((expected_size[0], expected_size[1]))
    # print(img.size)
    delta_width = expected_size[0] - img.size[0]
    delta_height = expected_size[1] - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding, fill='white')


if __name__ == "__main__":
    path = '/Users/muhannad/University/Masters-3rd/AdvMachineLearning/project/subset'
    new_p = '/Users/muhannad/University/Masters-3rd/AdvMachineLearning/project/finalizedSubset'
    
    for x in os.listdir(path):
        curr_path = os.path.join(path, x)
        new_path = os.path.join(new_p, x)
        img = Image.open(curr_path)
        img = resize_with_padding(img, (512, 512))
        img.save(new_path)