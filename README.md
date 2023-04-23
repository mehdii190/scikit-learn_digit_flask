# scikit-learn_digit_flask
scikit-learn dataset mnist digit with flask


### setup 

Download repository

Install libs from requirements.txt (may require installing non-python dependencies)

Train model or provide own (more info below)

Run app.py

Open your browser and navigate to http://127.0.0.1:5000/





![image](https://user-images.githubusercontent.com/92374066/233837649-bea896f6-8e7a-4104-8fc2-d4b6468e2260.png)







![image](https://user-images.githubusercontent.com/92374066/233837634-63631227-168c-4cac-a388-a8cdc06d2c8e.png)



### model training


Base model used project consists of two-step pipeline:

PCA reduces data dimensionality (wiki)
kNN classifier is used as a estimator (wiki)
During training, the following parameters are tuned:

PCA components count
Number of neighbours in kNN
metric used for calculating neighbour weight
To run model training run:






















