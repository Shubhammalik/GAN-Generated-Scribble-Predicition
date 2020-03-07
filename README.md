# Scribble-generation-using-GAN

Models - CNN, MLP, GAN, RF, 

This project aims at predicting scribbles from canvas and also using GAN generated images.

Idea was inspired from Kaggle's competition - https://www.kaggle.com/c/quickdraw-doodle-recognition/overview

Overview -

Trained a GAN model on few categories of objects from Quick Draw dataset. Save generated images in directory.(scribblegan.py)
Built a training model using a ConvNet and MLP Model (train.py).
Developed prediction model (server.py) which takes input from either canvas or GAN category dropdown (use saved images).
Tech Stack -

ML Libraries - Tensorflow, Keras, Scipy, Python
Webapp - Electron JS, HTML, JQuery and Flask App.
NOTE: This project works in Tensorflow 2.x with v1 compatibility.

Few images from WebApp and model -
