# import the matplotlib library
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# training data

# the first input feature for each data point
x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]

# the second input feature for each data point
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# the correct class for each data point
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# create a scatter plot using matlibplot which the two features on the axis and the colour representing the class
plt.scatter(x, y, c=classes)

# show the scatter plot
plt.show()

# ------------

# now we add a new data point and using KNN with K=1 to predict its class
# docs: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

# zip the data so that the data points are set as pairs
# https://www.w3schools.com/python/ref_func_zip.asp
data = list(zip(x, y))
# [(4, 21), (5, 19), (10, 24), (4, 17), (3, 16), (11, 25), (14, 24), (8, 22), (10, 21), (12, 21)]

# print to check the data
print(data)

# instantiate the model
knn = KNeighborsClassifier(n_neighbors=1)

# fit the model with the data
# this means passing the data with correct class labels into the model
# essentially training the model
knn.fit(data, classes)

# create a new data point
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

# ask the model to make a prediciton for the class of the new datapoint
prediction = knn.predict(new_point)
# returns predicted class of the new point

# add the new point with its class onto the previously generated 
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()

# ------------

# now we do the same thing with a much higher K value -> prediction changes

# instantiate a new classifier with a k value of 5
knn2 = KNeighborsClassifier(n_neighbors=5)

# fit the data to the model
knn2.fit(data, classes)

# make a prediciton on the new point
prediction = knn2.predict(new_point)

# add the new point to the scatter plot
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()