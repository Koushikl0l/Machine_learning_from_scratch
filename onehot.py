import numpy as np

def onehotencoding(label):
    ### convert label to numerical form or categorical
    mapping = {}
    for i,j in enumerate(np.unique(label)):
            mapping[j] = i
    
    # do onehot
    row_col = (len(label) ,len(np.unique(label)))
    arr = np.zeros(row_col,dtype=int)

    for i,c in enumerate(label):
        arr[i,mapping[c]] = 1

    return arr.tolist()

### Categorical data to be converted to numeric data
label = ["red", "green", "yellow", "red", "blue","red"]
print(onehotencoding(label))


