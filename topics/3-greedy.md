# Greedy Algorithms

## Class Scheduling Problem

## Knapsack problem

See worksheet.

## Storing Files on Tape

(4.1 in the textbook)

Consider storing $n$ files on magnetic tape.

Let $L[1..n]$ be an array listing the lengths of each file $i$.

The cost of accessing the *k*th file is:

$$
cost(k) = \sum_{i=1}^k L[i]
$$

Why? (We must scan past all other files on the tape).

The *expected* cost of reading a random file is

$$
E[cost] = \sum_{j=1}^n \frac{cost(j)}{n} = \frac{1}{n} \sum_{j=1}^n \sum_{i=1}^j L[i].
$$

What order should we use if we want this expected cost to be minimized?

The order is called a permutation, $\pi$. $\pi(i)$ denotes the index of the file
stored at position $i$ on the tape.

**Lemma 4.1.** $E[cost(\pi)]$ is minimized when $L[\pi(i)] \leq L[\pi(i+1)\]$ for
all $i$.

**Proof:** Suppose $L[\pi(i)] > L[\pi(i+1)]$ for some index $i$. Let $a=\pi(i)$
and $b=\pi(i+1)$. If we swap $a$ and $b$, then the cost of accessing $a$
increases by $L[b]$, and the cost of accessing $b$ decreases by $L[a]$. Overall,
the swap changes the expected cost by $(L[b]-L[a])/n$. But since $L[b] < L[a]$,
this decreases the expected cost.
