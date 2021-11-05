from math import sqrt
import random
import math
import matplotlib.pyplot as plt

def EuclidDist(point1, point2):

    distance = 0
    sum_of_dimensions = 0
    for idx in range(len(point1)):
        sum_of_dimensions += (point1[idx]-point2[idx])**2
    distance = sqrt(sum_of_dimensions)
    
    return distance


def FindClosestCentroid(point, centroid_list):
    
    distance_to_centroid = []
    for cluster_index in range(len(centroid_list)):
        distance = EuclidDist(point, centroid_list[cluster_index])
        distance_to_centroid.append(distance)
        
    min_distance = min(distance_to_centroid)
    closest_indx = distance_to_centroid.index(min_distance)
    min_centroid = centroid_list[closest_indx]
    
    return closest_indx


def InitEmptyClusters(k):
    clusters = []
    for i in range(k):
        clusters.append([])
    return clusters

def AssignItemsToClosestCluster(data_list, centroid_list):
    
    cluster_list = InitEmptyClusters(len(centroid_list))
        
    for key, data_point in data_list.items():

        closest_indx = FindClosestCentroid(data_point, centroid_list)
        cluster_list[closest_indx].append(key)
    
    return cluster_list

student_grades = {
    "Alice":(93, 88), "Bob":(55, 55), "Charles":(90, 87), "Dave":(63,57), "Ellen":(89,88), 
    "Frita":(96,94), "Grant":(70,86), "Heidi":(98,96), "Isabelle":(86,94), "Jack":(88,94), 
    "Kate":(60,86), "Lisa":(85,86), "Mary":(90,95), "Nancy":(63,58), "Orville":(88,61),
    "Peter":(95,58), "Quinton":(83,89), "Ralph":(57,65), "Sally":(67,65), "Trent":(62,62),
    "Ursala":(65,53), "Violet":(82,90), "Wally":(91,93), "Xavier":(81, 84), "Yolanda":(90, 63), "Zack":(85,56)
}
k = 3

def CaclulateCentroidLocation(data, cluster, dimension_count):
    
    centroid = [0] * dimension_count
    centroid = [0, 0]

    if len(cluster) > 0:

        for idx in range(dimension_count):
            
            centroid[idx] =   sum(data[cluster[i]][idx] for i in range(len(cluster)))
            centroid[idx] /=   len(cluster)
            
    return tuple(centroid)


def UpdateCentroidsKMeans(data, cluster_list):

    artibrary_cluster = cluster_list[0]
    arbitrary_key = artibrary_cluster[0]
    dimension_count = len(data[arbitrary_key])

    centroid_list = []

    for cluster in cluster_list:
        centroid_list.append(CaclulateCentroidLocation(data, cluster, dimension_count))


    return centroid_list

def CreateKMeansClusters(k, data, colors, x_label=None, y_label=None, max_passes=10, show_debug=True):

    stable_clusters = False
    pass_count = 0
    
    prev_centroids = ChooseRandomCentroids(student_grades, k)
    
    while stable_clusters == False and pass_count < max_passes:

        clusters = AssignItemsToClosestCluster(student_grades, prev_centroids)
        centroids = UpdateCentroidsKMeans(student_grades, clusters)

        if show_debug:
            PlotClusters2D(data, clusters, centroids, colors, x_label, y_label)

        if prev_centroids == centroids:
            stable_clusters = True
        prev_centroids = centroids
        pass_count += 1

        
        
        
    return (centroids, clusters)
    
colors = ["royalblue", "forestgreen", "maroon"]
CreateKMeansClusters(3, student_grades, colors, "Homework Scores", "Final Exam Scores")