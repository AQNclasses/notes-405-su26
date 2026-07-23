# Max Flows and Min Cuts

## Definitions

## Max-Flow Min-Cut Theorem

Proof:

Assume graph is reduced (no two-way directional edges). There is an easy way to
transform the graph if there are unreduced edges (see Fig. 10.4 in book).

Let $f$ be an arbitrary feasible (s,t)-flow in G.

We define a new capacity function, the residual capacity.

```math
c_f(u,v) = \begin{cases}
c(u,v) - f(u,v) & \text{if } (u,v) \in E \\
f(v,u) & \text{if } (v,u) \in E \\
0 & \text{otherwise}
\end{cases}
```

Observe that residual capacities are always non-negative.

The intuition is to define how much *more* flow can be pushed through that edge.

The **residual graph** is $(V, E_f)$ where $V$ is the original vertex set and
$E_f$ is the set of edges whose residual capacity is positive.
