import numpy as np
import requests
from PIL import Image
from io import BytesIO

def initalize_parameters(dim):
    w = np.zeros((dim, 1))
    b = 0.0
    return w, b

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(w, b, X):
    return sigmoid(np.dot(w.T, X) + b)

def propagate(w, b, X, Y):
    m = X.shape[1]
    A = logistic_regression(w, b, X)
    dw = (1/m)*np.dot(X, (A-Y).T)
    db = (1/m)*np.sum(A-Y)
    return dw, db

def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009):
    for _ in range(num_iterations):
        dw, db = propagate(w, b, X, Y)
        w -= learning_rate * dw
        b -= learning_rate * db
    return w, b

def predict(w, b, X):
    A = logistic_regression(w, b, X)
    Y_prediction = np.where(A > 0.5, 1, 0)
    return Y_prediction

def get_accuracy(w, b, X, Y):
    Y_prediction = predict(w, b, X)
    return 100 - np.mean(np.abs(Y_prediction - Y)) * 100

def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5):
    w, b = initalize_parameters(X_train.shape[0])
    w, b = optimize(w, b, X_train, Y_train, num_iterations, learning_rate)
    train_accuracy = get_accuracy(w, b, X_train, Y_train)
    test_accuracy = get_accuracy(w, b, X_test, Y_test)
    return {"w": w, "b": b, "train_accuracy": train_accuracy, "test_accuracy": test_accuracy}

def process_image(url, num_px):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = np.array(image)[:,:,:3]
    image = np.resize(image, (num_px, num_px, 3)) / 255 
    return image.reshape((1, num_px * num_px * 3)).T

def predict_image(url, model, classes, num_px):
    image = process_image(url, num_px)
    prediction = np.squeeze(predict(model["w"], model["b"], image))
    return classes[int(prediction)].decode("utf-8")