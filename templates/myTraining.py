import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


def data_split(data,ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indicies=shuffled[:test_set_size]
    train_indicies=shuffled[test_set_size:]
    return data.iloc[train_indicies], data.iloc[test_indicies]

if __name__=="__main__":
    df =pd.read_csv("coviddata.csv")
    train, test=data_split(df,.2)
    x_train=train[['age','fever','tiredness','loss of taste or smell','headache','diffbreath']].to_numpy()
    x_test=test[['age','fever','tiredness','loss of taste or smell','headache','diffbreath']].to_numpy()
    y_train=train[['infectionprob']].to_numpy().reshape(1700,)
    y_test=test[['infectionprob']].to_numpy().reshape(424,)
    clf=LogisticRegression()
    clf.fit(x_train,y_train)

    # open a file, where you ant to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(clf,file)
    file.close()

