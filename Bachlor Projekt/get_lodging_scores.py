import numpy as np
import pandas as pd
 
def get_labels():
    # read by default 1st sheet of an excel file
    dataframe1 =  pd.read_csv('Lodging_scores.csv', parse_dates=['VisualScoreDate','FlightDate'])
    scores = np.array(dataframe1)
    labels = []
    #create labels, [ROI, Visual SCORE, FLIGHTFolder]
    for i in range(scores.shape[0]):
        labels.append((scores[i,2], scores[i, 4], scores[i,6]))
    return labels