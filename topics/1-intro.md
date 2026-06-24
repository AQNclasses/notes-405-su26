# Introduction

Think-pair-share: What makes a "good" algorithm?

Is an efficient algorithm always good? Jevon's paradox.

We can analyze algorithms from multiple lenses:

- Resource Efficiency
- Practical usefulness, understandability
- Organizational culture
- Economics

## Computational model review

- RAM model
- loose definition of units
- most important thing is distinguishing constant time operations from non-constant time
- everything measured in terms of input size

## Course Structure

- approximately two weeks on greedy, dynamic, and randomized algorithm design
- rest of course shows applications in discrete combinatorial optimization (graph algorithms)
- search, shortest paths, matching, flows
- Writing point: writing, editing, revising
  - In and out of class

## Writing: Structuring an argument

- What is rhetoric?
- What is dialectic?
- What is a syllogism?

## Review of Induction

- Major premise: If something is true for $k$, it is true for $k+1$
- Minor premise: It is true for $k=0$
- Conclusion: It is true for all $k$

### Example 1: Handshaking

Claim: In any gathering of people, the number of people who shake hands an odd
number of times is always even.

Inductive step: Assume the rule is true for a room of k people. Now, bring in a
(k+1)-th person into the room. If this new person shakes hands with an even number
of existing people, the number of odd-handshakers doesn't change, keeping the
total count even. If the new person shakes hands with an odd number of existing
people, exactly that many people shift from having an even count to an odd count, preserving the even
total.

### Example 2: Tetrominoes

### Example 3: All Horses Are the Same Color
