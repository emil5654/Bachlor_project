import glob
import numpy as np
from skimage.io import imread

#Load all pictures in the folder
def read_img(img_list, img):
    n = imread(img)
    img_list.append(n)
    return img_list
def load_name_and_img(path):
    names = glob.glob(path)
    img_list_names = []
    img_list= []
    cv_image = [read_img(img_list, img) for img in names]
    return img_list, names
def it_name_extract_labels_from_img(names):
    plots = []
    temp = []
    for i in range(len(names)):
        name_t = names[i]
        #name_t = name_t.replace(".tif", "")
        for j in range(len(names[i])):
            if (names[i][j] == "\\"):
                temp.append(name_t[0:j])
        for j in range(1,len(name_t)):
            if (names[i][-j] == "_"):
                temp.append(name_t[-(j-1):len(name_t)].replace(".tif", ""))
                break
        plots.append(temp)
        temp = []
    return plots

def save_in_txt(save_array, filename):
    file = open(filename, "w+")
    # Saving the array in a text file
    np.save(filename, save_array)
    file.close()