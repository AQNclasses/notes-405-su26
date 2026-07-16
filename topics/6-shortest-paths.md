# Single Source Shortest Paths

## Assumptions:

- Directed Weighted Graph (easy to extend to unweighted case)
- No negative weights (will discuss later)

## Starting algorithm

Problem definition: can we find the shortest path from a single vertex to all
other vertices (efficiently)?

We will need to keep track of the distance to each node in a data structure
$dist$, and the predecessor of each node along the shortest path from the start,
in a data structure we will call $pred$. These may be cached in the graph nodes themselves, or you may build a separate "shortest path tree."

Check-in question: Is the shortest path tree the same as the minimum spanning
tree?

Basic algorithm to initialize the graph:

```
InitSSSP(s):
  dist(s) = 0
  pred(s) = null
  for all vertices v that are not s:
    dist(v) = Infinity
    pred(v) = null
```

Next, we define tense edges.

**Definition:** an edge $u \to v$ is tense if $dist(u) + w(u \to v) < dist(v)$,
implying the recorded distance at $v$ is an overestimate of the true shortest
path.

When we encounter a tense edge, we can relax the edge with the method:

```
Relax(u,v):
  dist(v) = dist(u) + w(u,v)
  pred(v) = u
```

## Ford's Algorithm

One line description: repeatedly relax tense edges, until there are no more
tense edges.

Specifically, we relax one edge at a time.

## Variations

### Breadth-first search

- Use queue, starting with just source vertex in queue
- Pull vertex, examine outgoing edges, if edge uv is tense, relax and push v
onto queue
- End when queue is empty


Runtime? Process each node and each edge at most once (proof in book); O(V+E).

### Depth-first search (only for DAGs)

If we are given a DAG, we can use depth first search in the *reversal* of the DAG to examine nodes in
topological order. The reversal is exactly what it sounds like: we reverse the direction of each directed edge. Again, O(V+E) time.

See also [Kahn's algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm) for another way to get nodes in topological order in a DAG (same worst-case complexity).

### Best-First: Dijkstra's Algorithm

Replace queue from BFS with priority queue, tackling minimum distance nodes
first.

Psuedocode:

```
Dijkstra(s):
  InitSSSP(s)
  Insert(s, 0) # add to priority queue (min-heap)
  while the priority queue is not empty
    u <- ExtractMin()
    for all edge u -> v
      if u->v is tense
        Relax(u,v)
        if v is in the priority queue
          DecreaseKey(v, dist(v))
        else
          Insert(v, dist(v))
```

Runtime: O(E log V) IF all edges are positive.

If we have negative edges, worst-case runtime is exponential (see book for
further discussion, but the intuition is that if negative edges exist, we 
may find a shortest path to a vertex v multiple times and will have to 
Extract v from the heap more than once).

### Bellman-Ford

The idea behind Bellman-Ford is to relax all tense edges before re-evaluating graph and 
looking for the next set of tense edges.

A neat feature of Bellman-Ford is that if the input graph has no negative cycles, the shortest
walk between any two vertices is a simple path with at most V-1 edges. This implies that Bellman-Ford
will have the correct shortest-path distances after V-1 iterations (can show via induction). An implication
is that if any edge is still tense after V-1 iterations, the input graph *must* contain a negative cycle, so 
we can use Bellman-Ford to check for negative cycles.

```
BellmanFord(s):
  InitSSSP(s)
  repeat V-1 times
    for every edge u->v
      if u->v is tense
        Relax(u,v)
  for every edge u->v
    if u->v is tense
      return "Negative cycle!"
```


Overall algorithm runs in O(VE) time, regardless of negative weights.

In practice, Dijkstra's algorithm is often faster, even with negative edges.

Proving correctness and runtime? See Lemma 8.6 in book.

Also see book for improvements that have same asymptotic runtime, but in practice are faster by avoiding checking edges that are not tense.

# Informed Search

We can build on Dijkstra's algorithm (best-first search) to improve path-finding
performance even more.

The idea is to build more information into the apparent "weights" of edges in
order to bias the search toward exploring solutions that are more likely to be
optimal.

The original motivation was path-planning for a mobile robot (Shakey) in the
1960s/1970s. They were trying to get Shakey to plan paths between start and goal
locations, but lacked the computational resources to do a full shortest-paths
search in the full graph (a discretized map of a building).

The algorithm is defined in terms of a specific goal node. The algorithm will
terminate once the shortest path to the goal is found, and will not build the
full shortest-paths tree, but it still builds a tree of paths.

The algorithm is called A* (said A star), for historical reasons, but this
started the naming convention of using the * symbol to denote an optimal version
of an algorithm.

At each iteration of the search, A* looks at the end node of each path and all
of its neighbors. For each neighbor $n$, we compute a cost

```math
f(n) = g(n) + h(n)
```

where $g(n)$ is the actual cost (sum of edge weights) of the path from the start
node to $n$, and $h(n)$ is a *heuristic* function that estimates the cost from
$n$ to the goal.

The correctness and optimality of A* depends on the heuristic function.

## Admissability

Specifically, the heuristic function must be *admissable*, defined as never
*overestimating* the cost of reaching the goal. In other words, the heuristic
must be a lower bound on the cost of reaching the goal from the current point in
the path.

For example, when searching in a 2D map that respects Euclidean geometry, $h(x)$
may be the straight-line distance from $x$ to the goal; it's the most optimistic
estimate of the remaining cost.

Another example is the [fifteen
puzzle](https://en.wikipedia.org/wiki/15_puzzle). For this puzzle, both the
Hamming distance (number of misplaced tiles) and the Manhattan distance
(sum of differences in Cartesian coordinates) are both admissable heuristics.

If the heuristic is admissable, A* is guaranteed to return an optimal solution.

## Consistency

However, if your heuristic is admissable but bad, A* may not do a very efficient
search. To guarantee efficiency, the heuristic must also be *consistent*. To be
consistent, the following property must hold for each node $u$ and its successor
$v$:

```math
h(u) \leq w(u,v) + h(v)
```

as well as the property that the heuristic estimates zero cost to reach the goal
from the goal: $h(g) = 0$ for goal node $g$.

This is a stronger property than admissability; in particular, all consistent
heuristics are admissable, but not all admissable heuristics are consistent.

The intuition is that by using a consistent heuristic, once A* has processed a
node, the cost to reach that node is the lowest possible and we will not need to
revisit the node to compute the actual shortest path.

In the sliding puzzle game, you could come up with a less-informative admissible
and consistent heuristic by only using the Manhattan distance of a subset of the
tiles. This will still only ever underestimate the number of moves to solve the
puzzle. If you choose two different subsets, and randomly select one to serve as
the heuristic during search, this heuristic is still admissable but is no longer
consistent: you are not guaranteed to have a monotonic relationship between
subsequent nodes.

## Analysis

Time complexity? Still $O(E log V)$, as A* is complete on finite graphs, but in practice much faster.

Space complexity is an issue, however, especially in large graphs. While it's
still a dynamic programming algorithm (best known solutions are memoized in the
graph itself or a data structure with the same size), the paths must be
enumerated and held in memory. This has led to the development of bounded-memory
heuristic search algorithms, which can still be proven to be correct and
complete.

It is also possible to speed up search by relaxing the optimality criterion;
then, we want to guarantee that the solution we find is no worse than
$(1+\epsilon)$ times the cost of the true optimal path.
