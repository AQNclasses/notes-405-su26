# Minimum Spanning Trees

define MST

define safe edges: the minimum-weight edge with exactly one endpoint in some component of F, where F is the "intermediate spanning forest"

define "useless" edges

# Borůvka's algorithm

- add all safe edges at the same time; repeat
- can lead to multiple trees being grown at the same time ("forest")
- O(E log V), but often much faster

# Prim's Algorithm

(really Jarnick's)

- start from arbitrary vertex to grow tree T. Add minimum-weight safe edge with one endpoint in T, one at a time to growing tree.
- O(E log V) time

# Kruskal's Algorithm

- sort safe edges by minimum weight, add minimum safe edge one at a time
- leads to multiple components at beginning ("forest")
- O(E log V)
