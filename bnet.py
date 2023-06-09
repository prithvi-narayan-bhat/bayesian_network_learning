from auxillary import *

DATASET_SIZE = 365                                                  # Number of samples in the dataset


def getConditionalProbability(dataSet, display):
    '''
        Function to calculate and display the conditional probabilities
    '''
    list_P = []
    dataFrame = getDataFrame(dataSet)

    # find sum of columns specified
    Bsum = dataFrame['B'].sum()                                     # Get number of true instances
    Csum = dataFrame['C'].sum()                                     # Get number of true instances

    P_B = float(Bsum / DATASET_SIZE)                                # Calculate base probability
    P_C = float(Csum / DATASET_SIZE)                                # Calculate base probability

    P_NB = float(1 - P_B)                                           # Calculate base probability
    P_NC = float(1 - P_C)                                           # Calculate base probability

    list_P.append(P_B)
    list_P.append(P_NB)
    list_P.append(P_C)
    list_P.append(P_NC)

    col = ['G', 'B']                                                # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (00, 01, 10, 11)

    # Probability is the ratio of the number of instances of each combination and size of the dataset
    P_GB    = (count[3] / DATASET_SIZE) / P_B                       # Calculate conditional probability
    P_GNB   = (count[2] / DATASET_SIZE) / P_NB                      # Calculate conditional probability
    P_NGB   = (count[1] / DATASET_SIZE) / P_B                       # Calculate conditional probability
    P_NGNB  = (count[0] / DATASET_SIZE) / P_NB                      # Calculate conditional probability

    list_P.append(P_GB)                                             # 4
    list_P.append(P_GNB)                                            # 5
    list_P.append(P_NGB)                                            # 6
    list_P.append(P_NGNB)                                           # 7

    col = ['G', 'C']                                                # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (00, 01, 10, 11)

    P_NGNC  = (count[0] / DATASET_SIZE)                             # Calculate probability
    P_NGC   = (count[1] / DATASET_SIZE)                             # Calculate probability
    P_GNC   = (count[2] / DATASET_SIZE)                             # Calculate probability
    P_GC    = (count[3] / DATASET_SIZE)                             # Calculate probability

    list_P.append(P_NGNC)                                           # 8
    list_P.append(P_NGC)                                            # 9
    list_P.append(P_GNC)                                            # 10
    list_P.append(P_GC)                                             # 11

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

    list_P.append(P_NFNGNC)                                         # 12
    list_P.append(P_NFNGC)                                          # 13
    list_P.append(P_NFGNC)                                          # 14
    list_P.append(P_NFGC)                                           # 15
    list_P.append(P_FNGNC)                                          # 16
    list_P.append(P_FNGC)                                           # 17
    list_P.append(P_FGNC)                                           # 18
    list_P.append(P_FGC)                                            # 19

    # Print calculated values of all probabilities
    if (display):
        data_B = [[P_B, P_NB]]                                      # Put values in a list to be printed later
        headers_B = ["B","NB"]                                      # Set the headers of the table to be printed

        data_C = [[P_C, P_NC]]                                      # Put values in a list to be printed later
        headers_C = ["C", "NC"]                                     # Set the headers of the table to be printed

        data_GB = [                                                 # Put values in a list to be printed later
            ["T", P_GB, P_NGB],
            ["F", P_GNB, P_NGNB]
        ]
        headers_GB = ["B", "P(G|B)", "P(!G|B)"]                     # Set the headers of the table to be printed

        data_FGC = [                                                # Put values in a list to be printed later
            ["T", "T", P_FGC, P_NFGC],
            ["T", "F", P_FGNC, P_NFGNC],
            ["F", "T", P_FNGC, P_NFNGC],
            ["F", "F", P_FNGNC, P_NFNGNC]
        ]

        headers_FGC = ["G", "C", "P(F|G,C)", "P(!F|G,C)"]           # Set the headers of the table to be printed

        prettyPrintData(data=data_B, header=headers_B)
        prettyPrintData(data=data_C, header=headers_C)
        prettyPrintData(data=data_GB, header=headers_GB)
        prettyPrintData(data=data_FGC, header=headers_FGC)
    else:
        return list_P

def getJointConditionalProbability(dataSet, states):
    dataFrame = getDataFrame(dataSet)

    states_list = states.split(" ")

    BGCF = validateStates(states_list)

    col = ['B', 'G', 'C', 'F']                                      # Set the columns of interest
    count = getCount(dataFrame=dataFrame, columns=col)              # Get the count of all combinations of these columns (00, 01, 10, 11)

    print(f"Given conditions: {states_list}\n")

    list_P = getConditionalProbability(dataSet, False)

    if  (BGCF == 0):    print(f"P(!F|!G,!C,!B): {float(list_P[1] * list_P[3] * list_P[7] * list_P[12])}")
    elif (BGCF == 1):   print(f"P(F|!G,!C,!B):  {float(list_P[1] * list_P[3] * list_P[7] * list_P[16])}")
    elif (BGCF == 2):   print(f"P(!F|!G,C,!B):  {float(list_P[1] * list_P[2] * list_P[7] * list_P[13])}")
    elif (BGCF == 3):   print(f"P(F|!G,C,!B):   {float(list_P[1] * list_P[2] * list_P[5] * list_P[17])}")
    elif (BGCF == 4):   print(f"P(!F|G,!C,!B):  {float(list_P[1] * list_P[3] * list_P[5] * list_P[14])}")
    elif (BGCF == 5):   print(f"P(F|G,!C,!B):   {float(list_P[1] * list_P[3] * list_P[5] * list_P[18])}")
    elif (BGCF == 6):   print(f"P(!F|G,C,!B):   {float(list_P[1] * list_P[2] * list_P[5] * list_P[15])}")
    elif (BGCF == 7):   print(f"P(F|G,C,!B):    {float(list_P[1] * list_P[2] * list_P[5] * list_P[19])}")
    elif (BGCF == 8):   print(f"P(!F|!G,!C,B):  {float(list_P[0] * list_P[3] * list_P[6] * list_P[12])}")
    elif (BGCF == 9):   print(f"P(F|!G,!C,B):   {float(list_P[0] * list_P[3] * list_P[6] * list_P[16])}")
    elif (BGCF == 10):  print(f"P(!F|!G,C,B):   {float(list_P[0] * list_P[2] * list_P[6] * list_P[13])}")
    elif (BGCF == 11):  print(f"P(F|!G,C,B):    {float(list_P[0] * list_P[2] * list_P[6] * list_P[17])}")
    elif (BGCF == 12):  print(f"P(!F|G,!C,B):   {float(list_P[0] * list_P[3] * list_P[4] * list_P[14])}")
    elif (BGCF == 13):  print(f"P(F|G,!C,B):    {float(list_P[0] * list_P[3] * list_P[4] * list_P[18])}")
    elif (BGCF == 14):  print(f"P(!F|G,C,B):    {float(list_P[0] * list_P[2] * list_P[4] * list_P[15])}")
    elif (BGCF == 15):  print(f"P(F|G,C,B):     {float(list_P[0] * list_P[2] * list_P[4] * list_P[19])}")

    print("\n\n")

def main():
    '''
        Function to calculate the probabilities of each possible condition
    '''
    dataSet = parseCli().dataSet                                   # Get dataset from user
    states = parseCli().conditions

    if parseCli().conditions != None:
        print("Calculating Joint Probability Distribution\n")
        getJointConditionalProbability(dataSet, states)

    else:
        print("Calculating Conditional Probability\n")
        getConditionalProbability(dataSet, display=True)

main()