# Computational Complexity

## Classifying

Consider the problem of analyzing an arbitrary Boolean circuit. The circuit tak
es in binary (0 or 1) inputs, combines the input values through AND, OR, and
NOT gates, and outputs a single bit, either 0 or 1. These circuits can be
converted to and from Boolean formulas. The complexity of the problem is
measured in terms of the total number of gates, which we will call $m$.

A classic "hard" problem in Computer Science is called "Circuit Satisfiability."
It asks whether there is any assignment of 0s and 1s to the inputs of the
circuit such that the circuit outputs 1.

![A boolean circuit made of AND, OR, and NOT gates. The circuit has five
inputs and one output.](circuit.png){width=200px}

Given a particular circuit and a set of inputs, it is easy to check (in time
polynomial in the number of gates $m$), whether a particular set of inputs
causes a 1 output. However, the decision problem is not solvable in polynomial
time, since there is no clever way around having to check all possible inputs,
which will take time exponential in the number of gates to evaluate.

## Fun Examples
