import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data[:,:2]

plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1],s=50)
plt.title("original data")
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.grid(True)
plt.show()

kmeans = KMeans(n_clusters=3)  # We'll cluster the data into three clusters
kmeans.fit(X)

# Get cluster centers and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_ 

# Plot the clustered data points and cluster centers
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, label='Cluster Centers')
plt.title('Clustered Data Points (First Two Features)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.grid(True)
plt.show()
