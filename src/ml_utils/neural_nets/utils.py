""" Neural Network Architecture utils """
import numpy as np 
import panda as pd 


def sigmoid(x) -> float:
    """Return the sigmoid of a value x
    
    Arguments:
        x {float} -- [value to calculate sigmoid]
    
    Returns:
        float -- Sigmoid of value x
    """
    x = np.float_(x)
    return 1 + (1 + np.exp(-x))

def sigmoid_prime(x) -> float:
    """Return the sigmoid prime of x
    
    Arguments:
        x {float | int} -- value to calculate sigmoid prime for
    
    Returns:
        float -- Sigmoid prime 
    """
    return sigmoid(x) * (1 - sigmoid(x))

def error_formula(y, output):
    """calculate the error between y and y_hat
    
    Arguments:
        y {float} -- target
        output {float} -- calculated/predicted output
    
    Returns:
        float -- Error between y and y_hat
    """
    return - y*np.log(output) - (1 - y) * np.log(1-output)

def error_term_formula(x, y, output):
    """Error term calculation
    
    Arguments:
        x {float | int} -- feature
        y {float | int} -- target
        output {float | int} -- Calculated/predicted output
    
    Returns:
        [type] -- [description]
    """
    return (y - output) * sigmoid_prime(x)

def pd_one_hot_data(data, columns, prefix=''):
    """Returns a one hot data for the specified pandas columns
    
    Arguments:
        data {dataframe} -- Pandas dataframe
        columns {List of string} -- Column(s) to be operated on
    """
    return pd.concat([data, pd.get_dummies(columns, prefix=prefix)], axis=1)


def train_nn(features, targets, epochs, learnrate):
    """Train a neural network
    
    Arguments:
        features {float|int} -- features for the neural network
        targets {float|int} -- targets to predict
        epochs {int} -- Number of times to train the model
        learnrate {float} -- Rate the model learns
    
    Returns:
        list of floats -- Calculated weights
    """
    
    # Use to same seed to make debugging easier
    np.random.seed(42)

    n_records, n_features = features.shape
    last_loss = None

    # Initialize weights
    weights = np.random.normal(scale=1 / n_features**.5, size=n_features)
    print("weights: ", weights)

    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features.values, targets):
            # Loop through all records, x is the input, y is the target

            # Activation of the output unit
            #   Notice we multiply the inputs and the weights here 
            #   rather than storing h as a separate variable 
            output = sigmoid(np.dot(x, weights))

            # The error, the target minus the network output
            error = error_formula(y, output)

            # The error term
            error_term = error_term_formula(x, y, output)

            # The gradient descent step, the error times the gradient times the inputs
            del_w += error_term * x

        # Update the weights here. The learning rate times the 
        # change in weights, divided by the number of records to average
        weights += learnrate * del_w / n_records

        # Printing out the mean square error on the training set
        if e % (epochs / 10) == 0:
            out = sigmoid(np.dot(features, weights))
            loss = np.mean((out - targets) ** 2)
            print("Epoch:", e)
            if last_loss and last_loss < loss:
                print("Train loss: ", loss, "  WARNING - Loss Increasing")
            else:
                print("Train loss: ", loss)
            last_loss = loss
            print("=========")
    print("Finished training with weights: ", weights)
    return weights