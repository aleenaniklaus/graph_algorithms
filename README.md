# Graph Algorithms SP19

This repository will be used for the majority of the term, and then migrated over to GitHub for public exposure. We want to make sure the repository is migrated to GitLab before the work is done, to show this is our original work.


Data Structure break down:
We chose to use an Adjacency list as represented as an array of arrays.

An alternative to the adjacency list is a sparce matrix. While
using sparce matricies is common, syntax is overly complex as
you must use Numpy/SciPy. Since these graphs are for proof of
concept, there is no reason to use such powerful structures at this point in time. Additionally, graphs will be small, thus the heavy-duty machinery behind Numpy is not necessary.

Lastly, the main advantage of adjacency list over matrix is 
the running/space complexity is lower at O(n) (verses O(n^2)). This implementation is aiming to keep costs low and will aim to create conclusions without iterating throughout the entire graph as most algorithms do. Instead, we aim to use countint arguments and facts about degrees of verticies amonst other facts of graphs.