# PCA (Unsupervised Method) + SVM (Supervised Method) Execution Code.
# Link: https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_eigenfaces.html
# Data: Face Images.
# Author: Shayan (Sean) Taheri - Jan/10/2021

# Simple facial recognition example: Labeled Faces in the Wild.
from sklearn import datasets
faces = datasets.fetch_olivetti_faces()
faces.data.shape

# Visualize these faces.
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(8, 6))
# plot several images
for i in range(15):
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.imshow(faces.images[i], cmap=plt.cm.bone)
plt.show()

# Localization and scaling to a common size.
# A typical train-test split on the images.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(faces.data,
        faces.target, random_state=0)

print(X_train.shape, X_test.shape)

# Use PCA to reduce these 1850 features to a manageable size
# while maintaining most of the information in the dataset.
from sklearn import decomposition
pca = decomposition.PCA(n_components=150, whiten=True)
pca.fit(X_train)

# Visualizing the PCA outcome. The "mean" image/data.
plt.imshow(pca.mean_.reshape(faces.images[0].shape),
           cmap=plt.cm.bone)
plt.show()

print(pca.components_.shape)

# Visualizing multiple PCA outcomes.
fig = plt.figure(figsize=(16, 6))
for i in range(30):
    ax = fig.add_subplot(3, 10, i + 1, xticks=[], yticks=[])
    ax.imshow(pca.components_[i].reshape(faces.images[0].shape),
              cmap=plt.cm.bone)
plt.show()

# The components (“eigenfaces”) are ordered by their importance
# from top-left to bottom-right.

# The components (“eigenfaces”) are ordered by their importance
# from top-left to bottom-right. We see that the first few
# components seem to primarily take care of lighting conditions;
# the remaining components pull out certain identifying
# features: the nose, eyes, eyebrows, etc.

# Project our original training and test data onto the PCA basis:
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print(X_train_pca.shape)

print(X_test_pca.shape)

# Perform support-vector-machine classification on this reduced dataset.
from sklearn import svm
clf = svm.SVC(C=5., gamma=0.001)
clf.fit(X_train_pca, y_train)

# Evaluate the classification performance.
# Plot a few of the test-cases with the labels learned from the training set.
import numpy as np
fig = plt.figure(figsize=(8, 6))
for i in range(15):
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.imshow(X_test[i].reshape(faces.images[0].shape),
              cmap=plt.cm.bone)
    y_pred = clf.predict(X_test_pca[i, np.newaxis])[0]
    color = ('black' if y_pred == y_test[i] else 'red')
    ax.set_title(y_pred, fontsize='small', color=color)
plt.show()

# Performance Evaluation
# sklearn.metrics: Do the classification report.
# The precision, recall, and other measures of
# the “goodness” of the classification
# The confusion matrix: Indicates how often any
# two items are mixed-up.

# The confusion matrix of a perfect classifier would
# only have nonzero entries on the diagonal, with
# zeros on the off-diagonal.
from sklearn import metrics
y_pred = clf.predict(X_test_pca)
print(metrics.classification_report(y_test, y_pred))

print(metrics.confusion_matrix(y_test, y_pred))