# Dynamic Programming


## Rod Cut


- Refer to Worksheet 1, "Rod Cut" problem

How to formulate a recursion for this problem?

Goal: find **optimal substructure**, such that the optimal solution to the
original problem incorporates optimal solutions to the subproblems.

At each stage of the algorithm, we are making one cut (or stopping and taking
revenue as-is).

To find revenue $r_n$, we search exhaustively over all possible options, finding the maximum over:

- $p_n$: the revenue from stopping here and making no more cuts.
- $r_1 + r_{n-1}$: max from a rod of size 1 and a rod of size $n-1$.
- $r_2 + r_{n-2}$: max from a rod of size 2 and a rod of size $n-2$.
- $\ldots$
- $r_{n-1} + r_1$

Written another way:

$$
r_n = \max \{ p_n, r_1 + r_{n-1}, \ldots, r_{n-1} + r_1 \}
$$

In functional notation:

$$
RodCut(n) = \max \{ p_n, RodCut(1) + RodCut(n-1), \ldots, RodCut(n-1) +
RodCut(1) \}
$$

Observations?

1. $p_n$ on its own is weird
2. Many repeated sub-problems

Reminder: *Recursion Trees* (draw on board, write down recurrence)

Another way to think of the problem: we cut off a rod at "the front", sell that
at price, and recurse on the remainder of the rod. Then, we are searching over
all lengths of rod to sell in the first step.

Can reformulate as:

$$
r_n = \max \{ p_i + r_{n-i} : 1 \leq i \leq n \}
$$

Still: many sub-problems, repeated. How to analyze performance?

We write down a **recurrence** that summarizes the performance of the
**recursive algorithm.**

# Top-down vs. Bottom-up

- See worksheet (Rod Cut 2)
- What is top-down?
- What is bottom-up?

## Maximum Independent Set in Trees

In graphs, the *maximum independent set* is the largest set of nodes where no
two nodes are directly adjacent. In general, this problem is NP-hard, but when
the graph is specifically a *tree*, we can do better.

For any node $v$ in a tree $T$, let $MIS(v)$ denote the size of the largest
independent set in the subtree rooted at $v$.

Note the problem structure: if $v$ is in the independent set, none of its
children can be. On the other hand, if $v$ is not in the independent set, the
union of independent sets of the subtrees rooted at $v$'s children is a valid
independent set for $T$.

Thus, we can write the recurrence:

```math
MIS(v) = \max \{ \sum_{w \in children(v)} MIS(w), 1 + \sum_{w \in child(v)}
\sum{x \in child(w)} MIS(x)}
```
