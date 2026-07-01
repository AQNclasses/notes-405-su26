# Graphs

- See Chapter 5.2 of Erickson for definitions we will be using in this course

Terms to know:

- node / vertex (plural: nodes / vertices)
  - same pattern: matrix/matrices, index/indices
- edge
- directed vs undirected
- *degree* (of a vertex): can narrow to in-degree and out-degree
- neighbor, adjacency
- edge weights
- *walk*: sequence of adjacent vertices
- *path*: a walk that visits each vertex in walk at most once
- vertex v is *reachable* from vertex u if there is a walk from u to v
- *connected*: in undirected graph specifically, if every vertex reachable from every other vertex
- *component*: maximal connected subgraph
- walk is *closed* if it starts and ends at same vertex
- cycle: a closed walk that enters and leaves each vertex at most once
- tree vs. graph (definition: tree is a connected acyclic graph)
- directed acyclic graphs (DAGs)


## Search

- Go over "anything first search" from Chapter 5
  - stack = depth first search
  - queue = breadth first search

Uses of graph search?

- Reachability:
  - find components of graphs (weak vs. strong components)
  - verify programs by computing all reachable states
  - flood fill
- Path planning
  - want to find a sequence of actions to get us from start to goal
- General Planning
  - Configuration graphs
  - knowledge graphs

## Analysis

### Adjacency list

Overall space required is O(V+E), where V is the number of vertices, and E is
the number of edges.

Get out-neighbors in O(1+deg(v)) time, where deg(v) is the degree of vertex v.

Check if edge uv exists in O(1+deg(u)) time.

Worst case? $O(V)$ for fully connected graph.

variation: adjacency array (show on board)

### Adjacency Matrix

$\Theta(1)$ time to check for existence of edge.

$O(V)$ time to find neighbors.

### Assumptions

Assume we use a standard adjacency list. Adjacency matrices are usually only
used for very dense graphs, or very dynamic graphs.

### Analyzing Search

We traverse each node at most once.

We traverse each edge at most twice.

Thus, assuming adjacency list, we have $O(V+E)$ for both BFS and DFS.

What if edges are comparable, and we want to choose minimum weight edges
earlier, to do "best first search"?

- If graph is undirected, and edges are weighted, best first search will find the minimum-weight spanning tree.
- If weight is interpreted as the length of an edge, we can find shortest paths.
- If weight is interpreted as a *width*, we can find "widest paths".

### Topological Search

Recall from trees: topological sort always gives us parents before children

How to extend this to directed graphs?

[See video on topological search](https://www.youtube.com/watch?v=cIBFEhD77b4)
