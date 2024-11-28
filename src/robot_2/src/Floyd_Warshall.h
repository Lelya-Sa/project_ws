//
// Created by lelyasa on 11/28/24.
//

#ifndef PROJECT_WS_FLOYD_WARSHALL_H
#define PROJECT_WS_FLOYD_WARSHALL_H

#include <limits.h>

// Number of vertices in the graph
#define V 13

/* Define Infinite as a large enough
value.This value will be used for
vertices not connected to each other */
#define INF INT_MAX

// A function to print the solution matrix
void printSolution(int dist[][V]);

#endif //PROJECT_WS_FLOYD_WARSHALL_H
