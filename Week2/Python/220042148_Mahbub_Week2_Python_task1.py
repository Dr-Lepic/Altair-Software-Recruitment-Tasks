import sys

NO_PARENT = -1

# !!!Source code is copied from:
# https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm
# then edited for desired output!!!

def dijkstra(adjacency_matrix, start_vertex, end_vertex):
    n_vertices = len(adjacency_matrix[0])
    start_vertex -= 1
    end_vertex -= 1

    # shortest_distances[i] will hold the
    # shortest distance from start_vertex to i
    shortest_distances = [sys.maxsize] * n_vertices

    # added[i] will true if vertex i is
    # included in shortest path tree
    # or shortest distance from start_vertex to
    # i is finalized
    added = [False] * n_vertices

    # Initialize all distances as
    # INFINITE and added[] as false
    for vertex_index in range(n_vertices):
        shortest_distances[vertex_index] = sys.maxsize
        added[vertex_index] = False

    # Distance of source vertex from
    # itself is always 0
    shortest_distances[start_vertex] = 0

    # Parent array to store shortest
    # path tree
    parents = [-1] * n_vertices

    # The starting vertex does not
    # have a parent
    parents[start_vertex] = NO_PARENT

    # Find shortest path for all
    # vertices
    for i in range(1, n_vertices):
        # Pick the minimum distance vertex
        # from the set of vertices not yet
        # processed. nearest_vertex is
        # always equal to start_vertex in
        # first iteration.
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        # Mark the picked vertex as
        # processed
        added[nearest_vertex] = True

        # Update dist value of the
        # adjacent vertices of the
        # picked vertex.
        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance

    print_solution(start_vertex, shortest_distances, parents, end_vertex)


# A utility function to print
# the constructed distances
# array and shortest paths
def print_solution(start_vertex, distances, parents, end_vertex):
    vertex_index = end_vertex
    if distances[vertex_index] != sys.maxsize:
        print("Path: ")
        print_path(vertex_index, parents)
    else:
        print(-1)


# Function to print shortest path
# from source to current_vertex
# using parents array
def print_path(current_vertex, parents):
    # Base case : Source node has
    # been processed
    if current_vertex == NO_PARENT:
        return
    print_path(parents[current_vertex], parents)
    print(current_vertex + 1, end=" ")


# Driver code
if __name__ == '__main__':
    n, edges = [int(n) for n in input().split()]
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(edges):
        x, y, weight = [int(x) for x in input().split()]
        x -= 1
        y -= 1
        adjacency_matrix[x][y] = weight

    dijkstra(adjacency_matrix, 1, n)
