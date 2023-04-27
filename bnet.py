from argparse import ArgumentParser as parser
import pandas as pd
import numpy as np
from pandas.core.common import flatten

DATASET_SIZE = 365

def getCount(dataFrame, columns):
    counts = dataFrame.groupby(columns).size()
    counts = pd.DataFrame(counts)
    counts = counts.values
    count = list(flatten(counts))

    return count

def parseCli():
    cli = parser()
    cli.add_argument('dataSet', help='Path to Training Dataset')
    cli_args = cli.parse_args()

    return cli_args


def getProbabilities():
    data_set = parseCli().dataSet

    columns = ['B', 'G', 'C', 'F']
    dataFrame = pd.read_csv(data_set, delimiter=' ', names=columns)

    # find sum of columns specified
    Bsum = dataFrame['B'].sum()
    Gsum = dataFrame['G'].sum()
    Csum = dataFrame['C'].sum()
    Fsum = dataFrame['F'].sum()

    # Fundamental values from table
    P_B = float(Bsum / DATASET_SIZE)
    P_G = float(Gsum / DATASET_SIZE)
    P_C = float(Csum / DATASET_SIZE)
    P_F = float(Fsum / DATASET_SIZE)

    P_NB = float(1 - P_B)
    P_NC = float(1 - P_C)
    P_NG = float(1 - P_G)
    P_GB = float((P_G * P_B) + (P_G * P_NB))

    col = ['B', 'G']
    count = getCount(dataFrame=dataFrame, columns=col)

    P_GB    = (count[0] / DATASET_SIZE) / P_NB
    P_GNB   = (count[1] / DATASET_SIZE) / P_NB
    P_NGB   = (count[2] / DATASET_SIZE) / P_B
    P_NGNB  = (count[3] / DATASET_SIZE) / P_B

    col = ['G', 'C']
    count = getCount(dataFrame=dataFrame, columns=col)
    print(count)
    print(P_C)

    P_GC    = (count[0] / DATASET_SIZE) / P_C
    P_GNC   = (count[1] / DATASET_SIZE) / P_C
    P_NGC   = (count[2] / DATASET_SIZE) / P_NC
    P_NGNC  = (count[3] / DATASET_SIZE) / P_NC

    print(P_GC, P_GNC, P_NGC, P_NGNC)


    col = ['G', 'C', 'F']
    count = getCount(dataFrame=dataFrame, columns=col)

    print(P_NGNC)
    print((count[0] / DATASET_SIZE) / P_NGNC)
    print((count[0] / DATASET_SIZE) / P_GC)
    print((count[0] / DATASET_SIZE) / P_GNC)
    print((count[0] / DATASET_SIZE) / P_NGC)

    (count[1] / 365) / P_GC
    (count[0] / 365) / P_GC
    (count[0] / 365) / P_GC
    (count[0] / 365) / P_GC
    (count[0] / 365) / P_GC
    (count[0] / 365) / P_GC


# print(f"P_B:  ", P_B)
# print(f"P_C:  ", P_C)
# print(f"P_NB: ", P_NB)
# print(f"P_NC: ", P_NC)
# print(f"P_GB: ", P_GB)

getProbabilities()