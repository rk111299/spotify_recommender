import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# psuedo code for recommendation algorithm

# 1. Work on a week's worth of data
# 2. min max normalise all the song attribute features
# 3. train / test split one week's data
# 4. k means clustering?

def train_k_means(df, k):
    """
    docstring 
    """
    kmeans = KMeans(n_clusters=k)

    kmeans.fit(df)

    cluster_labels = kmeans.labels_
    # centroids = kmeans.cluster_centers_

    df['cluster'] = cluster_labels