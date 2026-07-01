# Introduction

Think-pair-share: What makes a "good" algorithm?

Is an efficient algorithm always good? Jevon's paradox.

We can analyze algorithms from multiple lenses:

- Resource Efficiency
- Practical usefulness, understandability
- Organizational culture
- Economics

## Course Structure Overview

1. (Potentially) new methods: greedy algorithms, dynamic programming, randomized algorithms
2. Combinatorial and Discrete Optimization: shortest paths in graphs, matchings, flows/cuts
    - We will see demonstrations of methods from part 1 of the course in part 2 as we work with graph algorithms
3. Writing point: practicing writing and **revising**, mostly in the context of technical writing

We will interleave discussions of computational complexity theory and formal methods.

## Computational model review

- RAM model
- loose definition of units of (time/memory/etc): often defined during analysis of algorithm
- mostly important to distinguish "constant time" from other types of operations
    - constant in terms of **input size**
    - input size should be proportional to bits, but often we ignore details like the size of each element in an array with $N$ elements
    - can bound size of data on any actual machine
- single-processor model

## Algorithmic Problem Types

1. Decision problem: classify input as YES or NO
    - Example: Given a directed graph G, containing nodes $s$ and $t$, is there a path from $s$ to $t$?
2. Search problem: find a solution if input allows one, otherwise return NO SOLUTION
    - Completeness and correctness
    - Example: Given a directed graph G, containing nodes $s$ and $t$, return the nodes along a path from $s$ to $t$.
3. Optimization problem: find a *best* solution among all solutions, otherwise return NO SOLUTION
    - Example: Given a graph $G$, containing nodes $s$ and $t$, find a shortest path from $s$ to $t$.

## Computational Complexity

## Types of Problems

## Course Structure

- approximately two weeks on greedy, dynamic, and randomized algorithm design
- rest of course shows applications in discrete combinatorial optimization (graph algorithms)
- search, shortest paths, matching, flows
- Writing point: writing, editing, revising
  - In and out of class

## Writing: Structuring an argument

- What is dialectic?
- What is a syllogism?
- What is rhetoric?
