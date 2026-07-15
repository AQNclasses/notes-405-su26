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
