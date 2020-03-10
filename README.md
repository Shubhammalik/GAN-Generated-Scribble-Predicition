# Scribble-generation-using-GAN

Models - CNN, MLP, GAN, RF, 

This project aims at predicting scribbles from canvas and also using GAN generated images.

Idea was inspired from Kaggle's competition - https://www.kaggle.com/c/quickdraw-doodle-recognition/overview

# Overview

- Trained a GAN model on few categories of objects from Quick Draw dataset. Save generated images in directory.(scribble_generation_gan.py)

- Created script to download the data directly from the quick draw dataset website using [download_data.py](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/download_data.py).

- Built a training model using a ConvNet and MLP Model [train.py](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/train.py).

- Developed prediction model [server.py](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/server.py) which takes input from either canvas (from webapp) or GAN category dropdown (use saved images) and classify the scribbles among 7 categories.

- Presented the results on [webapplication](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/templates/index1.html).

# Tech Stack
1) ML Libraries - Tensorflow, Keras, Scipy, Python
2) Webapp - Electron JS, HTML, JQuery and Flask App.

**NOTE:** This project works in Tensorflow 2.x with v1 compatibility.

# Images WebApp and model
**Web Application**
![Web app](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/static/webapp.png)

**British Columbia Artificial Intelligence Showcase Poster**
![BC AI Poster](https://github.com/Shubhammalik/GAN-Generated-Scribble-Identification/blob/master/BC_AI_Showcase_Poster/BC%20AI%20showcase%20poster.png)

**GAN Generated sample**
![GAN sample](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/static/gan-final_chart.png)


**GAN Loss**
![GAN Loss](https://github.com/Shubhammalik/Scribble-generation-using-GAN/blob/master/static/gan-loss.png)
