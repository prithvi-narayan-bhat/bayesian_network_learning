# bayesian_network_learning
Simple example of the usage of Bayesian Networks and its implementation in python

## Author
* Prithvi Bhat | 1002033598
* +1(682)340-1126
* pnb3598@mavs.uta.edu


This code code is available on Github at the following link
#### https://github.com/prithvi-narayan-bhat/bayesian_network_learning

To clone the repository, enter the following command on a Git supported machine
#### git clone git@github.com:prithvi-narayan-bhat/bayesian_network_learning.git


## Execution
### System Requirements
The project was developed and tested on a Linux Mint machine (Kernel 5.15.0-56-generic) with Python3 (Version 3.10.6).
However, I am positive it can be run without any modifications on any compatible system
### Required Files
Ensure the the following files are all present in the same directory when executing
1. bnet.py
2. auxillary.py
3. Training_Data.py

### Command Line Execution

To run the application and perform any particular algorithm, run the following
##### python3 bnet.py [Training_Data] [-c "network_conditions"]
### [Training_Data]
This can be a text file or a csv of sampled data for the network

### [-c "network_conditions"] (optional)
This must be a string of characters followed by the delimiter -c. eg,  -c "B G C F"
The string of characters must include the states of all variables in the network in the particular order - B, G, C and F (if True)
The alternate acceptable values for these variables include - Bf, Gf, Cf, Ff (if False)
The requirement is that they must follow the order B-G-C-F and any combination of True/False within this order

### Execution Condition
#### B->G->F<-C
The assumed network in the system is
If the optional arguments are not provided, the system by default only calculates the Conditional Probability Values of nodes in the Bayesian Network
If the optional arguments are provided, the system calculates the Joint Probability Distribution of the given conditions