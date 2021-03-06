import loglinear as ll
import utils as ut
import random
import numpy as np

STUDENT = {'name': 'YOUR NAME',
           'ID': 'YOUR ID NUMBER'}

EPOCHS = 10
ETA = 0.1

def feats_to_vec(features):
    # YOUR CODE HERE.
    # Should return a numpy vector of features.
    feats_vec = np.zeros(len(ut.F2I))

    for bigram in features:
        index = ut.F2I.get(bigram)
        if index != None:
            feats_vec[index] += 1
    num_of_matches = np.sum(feats_vec)

    return feats_vec


def accuracy_on_dataset(dataset, params):
    good = bad = 0.0
    for label, features in dataset:
        # YOUR CODE HERE
        # Compute the accuracy (a scalar) of the current parameters
        # on the dataset.
        # accuracy is (correct_predictions / all_predictions)
        pass
    return good / (good + bad)


def train_classifier(train_data, dev_data, num_iterations, learning_rate, params):
    """
    Create and train a classifier, and return the parameters.

    train_data: a list of (label, feature) pairs.
    dev_data  : a list of (label, feature) pairs.
    num_iterations: the maximal number of training iterations.
    learning_rate: the learning rate to use.
    params: list of parameters (initial values)
    """
    for I in xrange(num_iterations):
        cum_loss = 0.0  # total loss in this iteration.
        random.shuffle(train_data)
        for label, features in train_data:
            x = feats_to_vec(features)  # convert features to a vector.
            y = label  # convert the label to number if needed.
            loss, grads = ll.loss_and_gradients(x, y, params)
            cum_loss += loss
            # YOUR CODE HERE
            # update the parameters according to the gradients
            # and the learning rate.

        train_loss = cum_loss / len(train_data)
        train_accuracy = accuracy_on_dataset(train_data, params)
        dev_accuracy = accuracy_on_dataset(dev_data, params)
        print I, train_loss, train_accuracy, dev_accuracy
    return params



if __name__ == '__main__':
    # YOUR CODE HERE
    # write code to load the train and dev sets, set up whatever you need,
    # and call train_classifier.

    params = ll.create_classifier(len(ut.F2I), len(ut.L2I))
    trained_params = train_classifier(ut.TRAIN, ut.DEV, EPOCHS, ETA, params)
