# K Cluster Classification
Generate a given number of random 2 dimensional points and place them into k classifications (4 and 2 in the output below) based on distance from a cluster center.

After all points are generated, select k points randomly as centroids. Then repeat the following steps until no further changes occur.

1. Classify all points based on euclidean distance, taking the closest centroid.
2. Adjust centroids (not the points they were originally based on) to a new location to the average of all x and y values of points in their cluster.

## Taken from final report for class
The starting seed is 95. Other tested seeds are: 50, 24, 127, 421, 379, 879, 801, 699, 555, and 333.

In both k = 2 and k = 4 presented below, distances for cluster 2 increased across multiple iterations. In k = 2, both types of distances for cluster 2 increase across all iterations. In k = 4, they increase until iteration 8 and will sometimes continue to increase. The TSSE values never increased, while the TSE value increased in exactly one iteration: iteration 10. It appears a cluster may increase its errors as long as the overall error (TSSE, at least) is decreasing.

Across every other seed, the trend continued. The only seeds that saw no increase in any cluster's error were those that needed only one iteration to complete. There were two cases where this occurred in k = 2 examples. Otherwise, every seed had at least one cluster that usually increased in error.

TSSE decreased in every case. TSE decreased in all but one case; during seed 333 on k = 2, TSE increased on iteration 4. The value changed from 1518.35 to 1519.23. However, TSSE still decreased on that iteration.

### Output

| Iteration # |	Clust#1       |            | Clust#2       |            | Clust#3       |            | Clust#4       |            | TSSE (sq-dist) | TSE (dist) |
| ----------- |:-------------:|:----------:|:-------------:|:----------:|:-------------:|:----------:|:-------------:|:----------:|:--------------:| ----------:|
|             |	Intra-sq-dist | Intra-dist | Intra-sq-dist | Intra-dist | Intra-sq-dist | Intra-dist | Intra-sq-dist | Intra-dist |                |            |
| 1           | 11929.74      | 471.45     | 101.3         | 14.23      | 292.02        | 32.55      | 20059.25      | 598.84     | 32382.3        | 1117.08    |
| 2           | 7916.24       | 362.14     | 999.17        | 72.19      | 1198.2        | 61.89      | 16134.06      | 506.52     | 26247.67       | 1002.75    |
| 3           | 5438.15       | 277.01     | 2026.69       | 128.14     | 1684.64       | 87.4       | 14966.32      | 471.31     | 24115.8        | 963.86     |
| 4           | 5438.15       | 277.01     | 2147.5        | 133.29     | 2054.69       | 105.3      | 13842.04      | 436.45     | 23482.38       | 952.06     |
| 5           | 5438.15       | 277.01     | 2979.76       | 175.31     | 2054.69       | 105.3      | 12138.31      | 375.93     | 22610.91       | 933.56     |
| 6           | 5438.15       | 277.01     | 2666.29       | 157.39     | 2270.49       | 121.99     | 12138.31      | 375.93     | 22513.23       | 932.32     |
| 7           | 5438.15       | 277.01     | 4497.79       | 201.5      | 2270.49       | 121.99     | 9936.72       | 330.67     | 22143.14       | 931.17     |
| 8           | 5438.15       | 277.01     | 4059.94       | 181.41     | 2526.49       | 139.9      | 9936.72       | 330.67     | 21961.29       | 928.99     |
| 9           | 5438.15       | 277.01     | 3423.17       | 155.63     | 2956.92       | 160.2      | 9936.72       | 330.67     | 21754.95       | 923.52     |
| 10          | 5438.15       | 277.01     | 5778.83       | 210.21     | 2956.92       | 160.2      | 7048.39       | 280.85     | 21222.3        | 928.27     |
| 11          | 5438.15       | 277.01     | 4363.85       | 180.42     | 3838.62       | 203.83     | 6111.6        | 253.36     | 19752.21       | 914.62     |
| 12          | 5438.15       | 277.01     | 4109.79       | 181.64     | 4332.04       | 224.74     | 4677.52       | 219.34     | 18557.49       | 902.73     |
| 13          | 5438.15       | 277.01     | 4559.49       | 203.38     | 4332.04       | 224.74     | 4075.21       | 197.47     | 18404.88       | 902.6      |

| Iteration # | Clust#1 |      | Clust#2 |     | TSSE (sq-dist) | TSE (dist) |
| ----------- |:-------------:|:----------:|:-------------:|:----------:|:--------------:| ----------:|
|             | Intra-sq-dist | Intra-dist | Intra-sq-dist | Intra-dist |                |            |
| 1           | 56742.68      | 1474.83    | 509.13        | 45.63      | 57251.81       | 1520.46    |
| 2           | 43985.38      | 1207.75    | 3510.49       | 183.44     | 47495.86       | 1391.2  |   
| 3           | 33933.49      | 969.7      | 8534.63       | 355.83     | 42468.12       | 1325.53 |   
| 4           | 29753.94      | 858.48     | 11694.72      | 452.18     | 41448.66       | 1310.66 |   
| 5           | 28881.76      | 828.57     | 12438.28      | 479.13     | 41320.04       | 1307.7  |
