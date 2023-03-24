import numpy as np # linear algebra

def match_pic_label_to_names(features, labels, names):
    n = len(labels)
    m = len(names)
    data_frame = []
    error = []
    for i in range(n):
        matched = False
        for j in range(m):
            if (str(labels[i][0]) == str(names[j][0]) and labels[i][2] == names[j][1]):
                data_frame.append(np.hstack((features[j], labels[i][3])))
                matched = True
        if (matched == False):
            error.append(np.hstack((labels[i][0], labels[i][2])))
    return data_frame, error

#error is images that has no labels
def match_pic_names_to_label(features, labels, names):
    m = len(labels)
    n = len(names)
    data_frame = []
    error = []
    for i in range(n):
        matched = False
        for j in range(m):
            if (str(labels[j][0]) == str(names[i][0]) and labels[j][2] == names[i][1]):
                data_frame.append(np.hstack((features[i], labels[j][3])))
                matched = True
        if (matched == False):
            error.append((names[i]))
    return data_frame, error