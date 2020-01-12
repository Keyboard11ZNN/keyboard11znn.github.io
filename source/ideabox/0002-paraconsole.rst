========================================================
The inadequacy of linear terminal for age of concurrency
========================================================

.. contents

Motivation
----------

The terminal interface was made with no user-level concurrency in mind.
When one uses build systems with support for automatic concurrency,
they have to deal with it. Their current solutions are unsatisfactory to
say the least.

Idea
----

Make a reception system that utilizes a growing tree of nodes.
A linear program can be relegated to a single node. A non-linear
program can delegate other programs to nodes and generate new ones.
Several different interfaces could be made to account for different
tastes. Automatic unfocusing of select elements, such as details of
successful unit compilations, could be implemented.

