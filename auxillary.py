from argparse import ArgumentParser as parser
from pandas.core.common import flatten
from tabulate import tabulate
import pandas as pd

def parseCli():
    '''
        Function to parse command line arguments
    '''
    cli = parser()
    cli.add_argument('dataSet', help='Path to Training Dataset')
    cli.add_argument("-c", "--conditions", help="states of B G C F (or Bf Gf Cf Ff in that order)")
    cli_args = cli.parse_args()

    return cli_args

def prettyPrintData(data, header):
    '''
        Function to pretty print calculated probability tables
    '''
    print(tabulate(data, headers=header, tablefmt="pipe"))
    print("\n\n\n")

def getCount(dataFrame, columns):
    '''
        Function to count number of instances of all combinations of the given headers
    '''
    counts = dataFrame.groupby(columns).size()                          # Extract dataset into a pandas dataFrame
    counts = pd.DataFrame(counts)                                       # Cleanup dataFrame
    counts = counts.values                                              # Some more cleanup
    count = list(flatten(counts))                                       # Convert them to a flat list

    return count

def getDataFrame(dataSet):
    '''
        Function read the given dataset and to convert it to a Pandas dataFrame
    '''
    columns = ['B', 'G', 'C', 'F']                                  # Set the expected data headers for the dataset
    dataFrame = pd.read_csv(dataSet, delimiter=' ', names=columns)  # Read dataset

    return dataFrame

def validateStates(states_list):
    BGCF = 0

    if (len(states_list) < 4):
        print("ERROR! Insufficient conditions provided")
        exit()

    else:
        if (states_list[3] == 'F'): BGCF = BGCF + (1<<0)
        elif (states_list[3] == 'Ff'): BGCF = BGCF + (0)
        else: print("Fourth argument does not provide information about F")

        if (states_list[2] == 'C'): BGCF = BGCF + (1<<1)
        elif (states_list[2] == 'Cf'): BGCF = BGCF + (0)
        else: print("Fourth argument does not provide information about C")

        if (states_list[1] == 'G'): BGCF = BGCF + (1<<2)
        elif (states_list[1] == 'Gf'): BGCF = BGCF + (0)
        else: print("Fourth argument does not provide information about G")

        if (states_list[0] == 'B'): BGCF = BGCF + (1<<3)
        elif (states_list[0] == 'Bf'): BGCF = BGCF + (0)
        else: print("Fourth argument does not provide information about B")

        return BGCF
