from click._compat import raw_input
from prepare_data import *
from sklearn.model_selection import train_test_split as tts
from keras.utils import np_utils
from nets.conv import conv
from random import randint
from download_data import read_classes, obtain_dataset
import numpy as np

# Read classes to download
out_classes = read_classes()

# Download datasets
#obtain_dataset(out_classes)

N_OBJECTS= len(out_classes)
OBJECTS = {}

for i in range(0, N_OBJECTS):
    OBJECTS[i] = out_classes[i]


# number of samples to take in each class
N = 2000

# Training epochs
N_EPOCHS = 20

# data files in the same order as defined in FRUITS
files = []

for i in range(0,N_OBJECTS):
    category = out_classes[i].replace(' ', '_')
    files.append(category+".npy")


# images need to be 28x28 for training with a ConvNet
objects = load("./datasets/", files, reshaped=True)

# limit no of samples in each class to N
objects = set_limit(objects, N)

# normalize the values
objects = list(map(normalize, objects))

# define the labels
labels = make_labels(N_OBJECTS, N)


# prepare the data
(x_train, x_test, y_train, y_test) = tts(objects, labels, test_size=0.05)

# one hot encoding
Y_train = np_utils.to_categorical(y_train, N_OBJECTS)
Y_test = np_utils.to_categorical(y_test, N_OBJECTS)

# use our custom designed ConvNet model
model = conv(classes=N_OBJECTS, input_shape=(28, 28, 1))

# use our custom designed MLP model
# model = mlp(classes=N_FRUITS)


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#raw_input("Type 'train' to start training: ")
print("Training commenced")

model.fit(np.array(x_train), np.array(Y_train), batch_size=32, epochs=N_EPOCHS, verbose=1)

print("Training complete")

print("Evaluating model")
preds = model.predict(np.array(x_test))

score = 0
for i in range(len(preds)):
    if np.argmax(preds[i]) == y_test[i]:
        score += 1

print("Accuracy: ", ((score + 0.0) / len(preds)) * 100)

name = raw_input(">Enter name to save trained model: ")
model.save("./models/"+ name + ".h5")
print("Model saved")


def visualize_and_predict():
    "selects a random test case and shows the object, the prediction and the expected result"
    n = randint(0, len(x_test))
    visualize(denormalize(np.reshape(x_test[n], (28, 28))))
    pred = OBJECTS[np.argmax(model.predict(np.array([x_test[n]])))]
    actual = OBJECTS[y_test[n]]
    print("Actual:", actual)
    print("Predicted:", pred)


print("Testing mode")
visualize_and_predict()