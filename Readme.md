# Stroke Prediction web app

# DISCLAIMER



## Summary

This is my second attempt experimenting with Neural Networks and Machine Learning.
I created  and trained a simple Neural Network model and a RandomForest model to predict whether or not  a patient is more likely to suffer from a stroke.
Both models are trained with the publicly available  [stroke prediction](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) dataset on Kaggle.
Then I created a simple REST API service with Flask to serve the models predictions based on HTTP requests


## Deep Neural Network

This is a simple dense neural network created with keras running on top of tensorflow. The model uses a tensor with size (19.1) as input,
which contains data from the data set and classifies whether a patient is more likely to have a stroke using multi-category classification
The classification is done using the softmax activation function which calculates the probability of the input tensor
belonging to each category respectively. 
The  model outputs an array with size (2,)  which holds in index 0 the probability of the patient not suffering from stroke in the near future  and in index 1 the
probability of  stroke happening

### Model Architecture 
```buildoutcfg
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
dense (Dense)                (None, 64)                1280
_________________________________________________________________
dropout (Dropout)            (None, 64)                0
_________________________________________________________________
dense_1 (Dense)              (None, 448)               29120
_________________________________________________________________
dropout_1 (Dropout)          (None, 448)               0
_________________________________________________________________
dense_2 (Dense)              (None, 2)                 898
=================================================================

Total params: 31,298
Trainable params: 31,298
Non-trainable params: 0
_________________________________________________________________
```