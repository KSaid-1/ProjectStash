# This code is to split the data into k-equal parts using Kfold from sklearn
# import the necessary packages
import pandas as pd
from sklearn import model_selection
from sklearn import datasets

input_path = '/Users/uqksaida/Desktop/ProjectStash/ProjectStash/mnist/Classification/input'
if __name__ == "__main__":
    # first let's get the data from sklearn
    data = datasets.fetch_openml('mnist_784',version=1,return_X_y=True)
    # create a dataframe
    df = pd.DataFrame(data[0])
    df['target'] = data[1]
    # create a new column called kfold and fill it with -1
    df['kfold'] = -1
    # shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)
    # initiate the kfold class from model_selection module
    kf = model_selection.KFold(n_splits=5)
    # fill the kfold column
    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df)):
        df.loc[val_idx, 'kfold'] = fold
    # save the new csv with kfold column
    df.to_csv(input_path+'/mnist_train_folds.csv', index=False)