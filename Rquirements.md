## Task 1
The Variables used here are as follows

-> B: True if there is a Baseball Game on TV, False if not
-> G: True if George watches TV, False if not
-> C: True if George is out of Cat Food, False if not
-> F: True if George feeds his cat, False if not.

Given a Training dataset which represents what happens every evening over one specific year and is formatted as follows
* The first number is 0 if there is no baseball game on TV (B is false), and 1 if there is a baseball game on TV (B is true).
* The second number is 0 if George does not watch TV (G is false), and 1 if George watches TV (G is true).
* The third number is 0 if George is not out of cat food (C is false), and 1 if George is out of cat food (C is true).
* The fourth number is 0 if George does not feed the cat (F is false), and 1 if George feeds the cat (F is true).

The task is to learn the conditional probability tables for the bayesian network from the training data.
The program should be called bnet and the command line invocation should follow the following format:

### bnet.py <training_data>
