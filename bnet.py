from argparse import ArgumentParser as parser
import pandas as pd
import numpy as np
from pandas.core.common import flatten
from tabulate import tabulate

DATASET_SIZE = 365                                                      # Number of samples in the dataset

def getCount(dataFrame, columns):
    '''
        Function to count number of instances of all combinations of the given headers
    '''
    counts = dataFrame.groupby(columns).size()                          # Extract dataset into a pandas dataFrame
    counts = pd.DataFrame(counts)                                       # Cleanup dataFrame
    counts = counts.values                                              # Some more cleanup
    count = list(flatten(counts))                                       # Convert them to a flat list

    return count

def parseCli():
    '''
        Function to parse command line arguments
    '''
    cli = parser()
    cli.add_argument('dataSet', help='Path to Training Dataset')
    cli_args = cli.parse_args()

    return cli_args


def getProbabilities():
    '''
        Function to calculate the probabilities of each possible condition
    '''
    data_set = parseCli().dataSet                                   # Get dataset from user

    columns = ['B', 'G', 'C', 'F']                                  # Set the expected data headers for the dataset
    dataFrame = pd.read_csv(data_set, delimiter=' ', names=columns) # Read dataset

    # find sum of columns specified
    Bsum = dataFrame['B'].sum()                                     # Get number of true instances
    Csum = dataFrame['C'].sum()                                     # Get number of true instances

    P_B = float(Bsum / DATASET_SIZE)                                # Calculate base probability
    P_C = float(Csum / DATASET_SIZE)                                # Calculate base probability
    P_NB = float(1 - P_B)                                           # Calculate base probability
    P_NC = float(1 - P_C)                                           # Calculate base probability

    data_B = [[P_B, P_NB]]                                          # Put values in a list to be printed later
    headers_B = ["B","NB"]                                          # Set the headers of the table to be printed

    data_C = [[P_C, P_NC]]                                          # Put values in a list to be printed later
    headers_C = ["C", "NC"]                                         # Set the headers of the table to be printed


    col = ['G', 'B']                                                # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (00, 01, 10, 11)

    # Probability is the ratio of the number of instances of each combination and size of the dataset
    P_GB    = (count[3] / DATASET_SIZE) / P_B                       # Calculate conditional probability
    P_GNB   = (count[2] / DATASET_SIZE) / P_NB                      # Calculate conditional probability
    P_NGB   = (count[1] / DATASET_SIZE) / P_B                       # Calculate conditional probability
    P_NGNB  = (count[0] / DATASET_SIZE) / P_NB                      # Calculate conditional probability

    data_GB = [                                                     # Put values in a list to be printed later
        ["T", P_GB, P_NGB],
        ["F", P_GNB, P_NGNB]
    ]

    headers_GB = ["B", "P(G|B)", "P(!G|B)"]                         # Set the headers of the table to be printed

    col = ['G', 'C']                                                # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (00, 01, 10, 11)

    P_NGNC  = (count[0] / DATASET_SIZE)                             # Calculate probability
    P_NGC   = (count[1] / DATASET_SIZE)                             # Calculate probability
    P_GNC   = (count[2] / DATASET_SIZE)                             # Calculate probability
    P_GC    = (count[3] / DATASET_SIZE)                             # Calculate probability

    col = ['F','G', 'C']                                            # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (000, 001, 010, 011, ..)

    P_NFNGNC    = ((count[0] / DATASET_SIZE) / P_NGNC)              # Calculate conditional probability
    P_NFNGC     = ((count[1] / DATASET_SIZE) / P_NGC)               # Calculate conditional probability
    P_NFGNC     = ((count[2] / DATASET_SIZE) / P_GNC)               # Calculate conditional probability
    P_NFGC      = ((count[3] / DATASET_SIZE) / P_GC)                # Calculate conditional probability
    P_FNGNC     = ((count[4] / DATASET_SIZE) / P_NGNC)              # Calculate conditional probability
    P_FNGC      = ((count[5] / DATASET_SIZE) / P_NGC)               # Calculate conditional probability
    P_FGNC      = ((count[6] / DATASET_SIZE) / P_GNC)               # Calculate conditional probability
    P_FGC       = ((count[7] / DATASET_SIZE) / P_GC)                # Calculate conditional probability

    data_FGC = [                                                    # Put values in a list to be printed later
        ["T", "T", P_FGC, P_NFGC],
        ["T", "F", P_FGNC, P_NFGNC],
        ["F", "T", P_FNGC, P_NFNGC],
        ["F", "F", P_FNGNC, P_NFNGNC]
    ]

    headers_FGC = ["G", "C", "P(F|G,C)", "P(!F|G,C)"]               # Set the headers of the table to be printed

    # Print calculated values of all probabilities
    print("Probabilities of B\n")
    print(tabulate(data_B, headers=headers_B, tablefmt="pipe"))

    print("\n\nProbabilities of C\n")
    print(tabulate(data_C, headers=headers_C, tablefmt="pipe"))

    print("\n\nProbabilities of G, dependent on B\n")
    print(tabulate(data_GB, headers=headers_GB, tablefmt="pipe"))


    print("\n\nProbabilities of F, dependent on G and C\n")
    print(tabulate(data_FGC, headers=headers_FGC, tablefmt="pipe"))
    print("\n\n\n\n")

getProbabilities()