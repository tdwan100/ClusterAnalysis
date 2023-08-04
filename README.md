# K-Means Clustering for Student Grades

This repository contains a Python implementation of the K-Means clustering algorithm for analyzing student grades. The K-Means algorithm is a popular unsupervised learning method used to partition data into K clusters based on similarity. In this case, we will cluster students based on their homework scores and final exam scores.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [EuclidDist](#eucliddist)
  - [FindClosestCentroid](#findclosestcentroid)
  - [InitEmptyClusters](#initemptyclusters)
  - [AssignItemsToClosestCluster](#assignitemstoclosestcluster)
  - [CaclulateCentroidLocation](#caclulatecentroidlocation)
  - [UpdateCentroidsKMeans](#updatecentroidskmeans)
  - [CreateKMeansClusters](#createkmeansclusters)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- matplotlib library

## Installation

To use the K-Means clustering for student grades, make sure you have Python 3.x installed. You can install the matplotlib library using pip:

```
pip install matplotlib
```

## Usage

Clone this repository to your local machine to access the K-Means clustering functions.

```
git clone https://github.com/your-username/k-means-clustering.git
```

## Functions

### EuclidDist

The `EuclidDist` function calculates the Euclidean distance between two data points.

### FindClosestCentroid

The `FindClosestCentroid` function finds the closest centroid to a given data point.

### InitEmptyClusters

The `InitEmptyClusters` function initializes an empty list of clusters.

### AssignItemsToClosestCluster

The `AssignItemsToClosestCluster` function assigns data points to their closest cluster.

### CaclulateCentroidLocation

The `CaclulateCentroidLocation` function calculates the centroid location based on the data points in a cluster.

### UpdateCentroidsKMeans

The `UpdateCentroidsKMeans` function updates the centroids based on the current clusters.

### CreateKMeansClusters

The `CreateKMeansClusters` function performs the K-Means clustering for the given data.

## Example

You may alter the input data and output colors to use in the K-Means clustering function here:


```
student_grades = {
    "Alice":(93, 88), "Bob":(55, 55), "Charles":(90, 87), "Dave":(63,57), "Ellen":(89,88), 
    "Frita":(96,94), "Grant":(70,86), "Heidi":(98,96), "Isabelle":(86,94), "Jack":(88,94), 
    "Kate":(60,86), "Lisa":(85,86), "Mary":(90,95), "Nancy":(63,58), "Orville":(88,61),
    "Peter":(95,58), "Quinton":(83,89), "Ralph":(57,65), "Sally":(67,65), "Trent":(62,62),
    "Ursala":(65,53), "Violet":(82,90), "Wally":(91,93), "Xavier":(81, 84), "Yolanda":(90, 63), "Zack":(85,56)
}

colors = ["royalblue", "forestgreen", "maroon"]
```

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
