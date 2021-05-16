from tensorflow import keras
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier


def predict(data):
    random_forest = pickle.load(open("../model/RandomForest.sav", 'rb'))
    neural_network = keras.models.load_model("../model/NeuralNetwork.h5")

    data = np.array(data).reshape(1,-1)

    predictions = {}

    predictions['neural_network'] = neural_network.predict(data)

    predictions['random_forest']  = random_forest.predict(data)

    return  predictions


if __name__ == "__main__":
    print(predict([62,1,0,0,0,0,1,1,100,28,0,0,0,1,0,0,0,1,0]))