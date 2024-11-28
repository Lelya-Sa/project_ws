//
// Created by lelyasa on 11/28/24.
//

#include "Floyd_Warshall.h"
// C++ Program for Floyd Warshall Algorithm
#include <bits/stdc++.h>
#include <iostream>
#include <cmath>
using namespace std;

// Function to calculate distance
double distance(double x1, double y1, double x2, double y2) {
    return std::sqrt(std::pow((x2 - x1), 2) + std::pow((y2 - y1), 2));
}

// Solves the all-pairs shortest path
// problem using Floyd Warshall algorithm
void floydWarshall(int dist[][V])
{

    int i, j, k;

    /* Add all vertices one by one to
    the set of intermediate vertices.
    ---> Before start of an iteration,
    we have shortest distances between all
    pairs of vertices such that the
    shortest distances consider only the
    vertices in set {0, 1, 2, .. k-1} as
    intermediate vertices.
    ----> After the end of an iteration,
    vertex no. k is added to the set of
    intermediate vertices and the set becomes {0, 1, 2, ..
    k} */
    for (k = 0; k < V; k++) {
        // Pick all vertices as source one by one
        for (i = 0; i < V; i++) {
            // Pick all vertices as destination for the
            // above picked source
            for (j = 0; j < V; j++) {
                // If vertex k is on the shortest path from
                // i to j, then update the value of
                // dist[i][j]
                if (dist[i][j] > (dist[i][k] + dist[k][j])
                    && (dist[k][j] != INF
                        && dist[i][k] != INF))
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    // Print the shortest distance matrix
    printSolution(dist);
}

/* A utility function to print solution */
void printSolution(int dist[][V])
{
    cout << "The following matrix shows the shortest "
            "distances"
            " between every pair of vertices \n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF)
                cout << "INF"
                     << " ";
            else
                cout << dist[i][j] << "   ";
        }
        cout << endl;
    }
}

int eul

//// Driver's code
int main()
{
    /* Let us create the following complete weighted graph of vertices:
DispatchA   -9 9 0 0 -0 0   -9 9 0 0 -0 0red_1_3_right  -1.15 -3.5 0.65 0 -0 0   -0.75 -3.5 0.65 0.0 0.0 -3.14159
red_1_4_right   0.34 -3.5 0.65 0 -0 0   0.74 -3.5 0.65 0.0 0.0 -3.14159
red_1_5_right   1.84 -3.5 0.65 0 -0 0   2.24 -3.5 0.65 0.0 0.0 -3.14159
red_4_3_right  -1.15 6.4 0.65 0 -0 0   -0.75 6.4 0.65 0.0 0.0 -3.14159
red_4_4_right  0.34 6.4 0.65 0 -0 0   0.74 6.4 0.65 0.0 0.0 -3.14159
red_4_5_right   1.84 6.4 0.65 0 -0 0   2.24 6.4 0.65 0.0 0.0 -3.14159
 */


    int graph[V][V] ;
    for (int i=0; i<V; i++){
        for (int k = 0; k<V; k++){

        }
    }

    // Function call
    floydWarshall(graph);
    return 0;
}

// This code is contributed by Mythri J L