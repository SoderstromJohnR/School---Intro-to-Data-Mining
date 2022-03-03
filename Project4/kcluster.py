####################################
# Author: John Soderstrom
# Due: 5/13/2020
#
# Randomly generate a given number of 2D points (1.0 <= x, y <= 100.0)
# and divide them into 2 or 4 clusters. Scales to any number of clusters,
# as long as they do not outnumber the points.
#
# Uses euclidean distance to judge nearby clusters.
#
# Centroids are randomly selected from the random points before
# being adjusted with every iteration. The program ends when
# centroids do not move from the previous iteration.
#
# With a little more work, this program could scale not just to the
# number of clusters, but also the number of dimensions. For now, this
# program merely works with 2D points.
#####################################

import random
import copy
from pprint import pprint as pp

###
# Stores randomly generated points given bounds, and creates/tracks
# centroids. Tracks the number of iterations, and prints results
# with formatting to screen as they happen.
###
class Clusters:
    def __init__(self, kVal, numPoints, minX, maxX, minY, maxY):
        self.kVal = kVal
        self.numPoints = numPoints
        self.iterations = 0
        self.points = []
        self.centroids = []
        self._generatePoints(minX, maxX, minY, maxY)
        self._generateCentroids()
        self._printHeader()
        self._iterate()

    ###
    # Given bounds and number of points to generate, fills a
    # list with 2D point data. An extra element is added to
    # track which cluster they will be part of.
    ###
    def _generatePoints(self, minX, maxX, minY, maxY):
        for i in range(self.numPoints):
            tempX = random.uniform(minX, maxX)
            tempY = random.uniform(minY, maxY)
            self.points.append([tempX, tempY, -1])

    ###
    # After points are generated, randomly select a given number
    # equal to the number of clusters as centroids from the points.
    ###
    def _generateCentroids(self):
        indices = random.sample(range(self.numPoints), self.kVal)
        for i in indices:
            self.centroids.append(self.points[i][:-1].copy())

    ###
    # Get the euclidean distance between two points. This doubles
    # as the error from various points to the mean, or their centroid.
    ###
    def _euclid(self, p1, p2):
        dist = 0
        for i in range(len(p1) - 1):
            dI = p1[i] - p2[i]
            dist += dI * dI
        return pow(dist, .5)

##    def _dist(self, p1, p2):
##        dist = 0
##        for i in range(len(p1) - 1):
##            dI = p1[i] - p2[i]
##            dist += abs(dI)
##        print(dist)
##        return dist

    ###
    # Gets the squared distance between two points. Used to output
    # information to the screen from print statements.
    ###
    def _distSq(self, p1, p2):
        dist = 0
        for i in range(len(p1) - 1):
            dI = p1[i] - p2[i]
            dist += dI * dI
        return dist

    ###
    # Assign points to clusters and update centroids. Repeat
    # until centroids do not change from previous iteration.
    # Prints for each iteration except the last, the repeat.
    ###
    def _iterate(self):
        keepIter = True
        while keepIter:
            self._setClusters()
            testUpdate = self._updateCentroids()
            keepIter = self._checkUpdatedCentroids(testUpdate)
            self.iterations += 1
            if keepIter:
                self._printLine()

    ###
    # Assign each point to a centroid. Finds the euclidean distance
    # from a point to all centroids and selects the one that is closest.
    # The centroid number takes the last element's place in each point.
    ###
    def _setClusters(self):
        for count, i in enumerate(self.points):
            nearDist = -1
            for countCent, j in enumerate(self.centroids):
                tempDist = self._euclid(i, j)
                if nearDist > tempDist or nearDist is -1:
                    nearDist = tempDist
                    self.points[count][-1] = countCent

    ###
    # Returns a list containing the updated centroids after an
    # iteration. Quickly cycles through all points adding their
    # values to the updated centroid list, tracking the number
    # of points for each centroid. Divides the final result by
    # that number to get the mean.
    ###
    def _updateCentroids(self):
        numPoints = [0] * self.kVal
        nextCentroid = []
        for i in range(self.kVal):
            nextCentroid.append([0, 0])
        
        for countPoint, i in enumerate(self.points):
            numPoints[i[-1]] += 1
            for j in range(len(i) - 1):
                nextCentroid[i[-1]][j] += i[j]

        for count, i in enumerate(numPoints):
            for j in range(len(self.centroids[0])):
                nextCentroid[count][j] /= i
                
        return nextCentroid

    ###
    # Given a list of new centroids, checks them against the
    # previous list. If any differences are found, assign the updated
    # values to the actual centroids and return early. Returning False
    # means there are no changes and iterations can stop.
    ###
    def _checkUpdatedCentroids(self,testUpdate):
        for countPoint, i in enumerate(testUpdate):
            for countPart, j in enumerate(i):
                if abs(j - self.centroids[countPoint][countPart]) > .0001:
                    self.centroids = testUpdate
                    return True
        return False

    ###
    # Given the number associated with a centroid/cluster, sum all
    # the squared distances between the centroid and all points
    # within the cluster. Return the sum.
    ###
    def _clustDistSq(self, clustNum):
        dist = 0
        for i in self.points:
            if i[-1] is clustNum:
                dist += self._distSq(i, self.centroids[clustNum])
        return dist

    ###
    # Given the number associated with a centroid/cluster, sum all
    # the distances between the centroid and all points within
    # the cluster. Return the sum.
    ###
    def _clustDist(self, clustNum):
        dist = 0
        for i in self.points:
            if i[-1] is clustNum:
                dist += self._euclid(i, self.centroids[clustNum])
        return dist

    ###
    # Called once at the start. Prints two formatted lines with header
    # information for the final table. Cluster specific information is
    # scaled to the number of clusters.
    ###
    def _printHeader(self):
        # Line 1, most important information here
        headFormat = ['Iteration #']
        headString = '{:<13s}'
        for i in range(self.kVal):
            headFormat.append('Clust#{}'.format(i + 1))
            headString += '{:<25s}'
        headFormat.append('TSSE (sq-dist)')
        headFormat.append('TSE (dist)')
        headString += '{:<15s}{:<11s}'
        print(headString.format(*headFormat))

        # Line 2, divides up cluster specific columns
        headFormat = ['']
        headString = '{:<13s}'
        for i in range(self.kVal):
            headFormat.append('Intra-sq-dist')
            headFormat.append('Intra-dist')
            headString += '{:<14s}'
            headString += '{:<11s}'
        print(headString.format(*headFormat))

    ###
    # Called once for each iteration. Prints a formatted string
    # containing iteration number, error values across clusters,
    # and error values specific to each cluster.
    ###
    def _printLine(self):
        lineString = '{:<13s}'
        lineFormat = [str(self.iterations)]
        tsse = 0
        tse = 0
        for i in range(self.kVal):
            lineString += '{:<14s}'
            lineString += '{:<11s}'
            tempSq = self._clustDistSq(i)
            tempDist = self._clustDist(i)
            tsse += tempSq
            tse += tempDist
            lineFormat.append(str(round(tempSq, 2)))
            lineFormat.append(str(round(tempDist, 2)))
        lineString += '{:<15s}{:<11s}'
        lineFormat.append(str(round(tsse, 2)))
        lineFormat.append(str(round(tse, 2)))
        print(lineString.format(*lineFormat))

# Checking for "bad" seeds that required more iterations than most (on 4 clusters), I got these:
#  (seeds, iterations): (0, 13), (10, 14), (53, 16), (189, 19), (209, 21), (592, 27)
# Then I realized I did that for 100 points when we only needed 50.
# Doing it again for 50 points got the following:
#  (18, 11), (25, 12), (64, 13), (95, 14), (284, 15), (580, 16)
random.seed(333)
numPoints = 50
numClust = 2
minX = minY = 1.0
maxX = maxY = 100.0

test = Clusters(numClust, numPoints, minX, maxX, minY, maxY)
#test._iterate()
