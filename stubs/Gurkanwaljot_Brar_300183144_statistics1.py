######### Pseudocode ##########
# Step1 - From math import square root.
# Step2 - Define a function 'mean' having variable as 'incomeList'
#   Step2.1 - Set numberOfEmployees equal to size of the variable 'incomeList'
#   Step2.2 - Set total equal to zero.
#   Step2.3 - For 'income' in variable 'incomeList',
#                   Set 'total' equal to sum of 'total' and 'income'
#   Step2.4 - Set 'variable' equal to 'total' divided by 'numberOfEmployees.
#   Step2.5 - Return variable 'average'.
# Step3 - Define a function 'standardDeviation' having variable 'incomeList' and 'mean' 
#   Step3.1 - Set variable 'stdDev' equal to zero.
#   Step3.2 - Set 'numberOfEmployees' equal to size of the variable 'incomeList'.
#   Step3.3 - For 'income' in 'incomeList',
#               Set 'stdDev' equal to sum of 'stdDev' and sqaure of subtraction of 'mean' and 'income' which is divided by the variable 'numberOfEmployees'
#   Step3.4 - Set 'stdDev' equal to sqaure root of variable 'stdDev'.
#   Step3.5 - Retrun 'stdDev'.
# Step4 - Define a function 'median' having a variable 'incomeList'
#   Step4.1 - Set 'numberOfEmployees' equal to size of the variable 'incomeList'
#   Step4.2 - Now sort the variable 'incomeList' in order to calculate the median.
#   Step4.3 - If 'numberOfEmployees' is divided by 2, having a remainder equal to zero that is the incomeList is an even list,
#               Set 'median1' to the value which is the first middle value of the 'incomeList' if the 'incomeList' by dividing 'numberOfEmployees' by 2
#               Set 'median2' to the value which is the second middle value of the 'incomeList' if the 'incomeList' by dividing 'numberOfEmployees' by 2 and then subtracted by 1.
#               Set 'median' equal to sum of 'median1' and 'median2'and then divided by 2.
#   Step4.4 - Else the incomeList is an odd number list, then
#               Set 'median' to the value which is the middle value of the 'incomeList' if the 'incomeList' by dividing 'numberOfEmployees' by 2
#   Step4.5 - Return 'median'.
# Step5 - Define a function 'computeModes' having variable 'incomelist'
#   Step5.1 - Set an empty list under the name 'dicitonaryList'.
#   Step5.2 - Create an dictionaries which store the values from the steps below
#   Step5.3 - Set 'max_count' equal to zero
#   Step5.4 - For 'income' in 'incomeList',
#       Step5.4.1 The formula: dictionaries[income] = dictionaries.get(income, 1) + 1, here checks whether the 'income' exist in dictionary:
#                     1)If the 'income' is not in the dictionaries then return value to be zero and increments value by 1 
#                     2)If the 'income' exist in the dictionaries then counts the value in it and then increments value by 1.
#       Step5.4.2     If the dictionaries[income] is greater than max_count, then
#                         Set max_count equal to dictionaries[income].
#   Step5.5 - For income, dictionary in dictionaries.get():
#       Step5.5.1 If the dictonary is equal to the max_count, then
#                   append the values of income in the dictionaryList.
#   Step5.6 - Return dictionaryList.



from math import sqrt                                                                                               #Step1                                                                                 

#function computes mean or average of a set of numbers
def mean( incomeList ) :                                                                                            #Step2
    numOfEmployees = len(incomeList)                                                                                #Step2.1
    total = 0                                                                                                       #Step2.2
    for income in incomeList:                                                                                       #Step2.3
        total += income

    average = total / numOfEmployees                                                                                #Step2.4
    return average                                                                                                  #Step2.5

    
#function computes the standard deviation of a set of numbers
def standardDeviation( incomeList, mean ) :                                                                         #Step3
    stdDev = 0                                                                                                      #Step3.1
    numberOfEmployees = len(incomeList)                                                                             #Step3.2
    for income in incomeList:                                                                                       #Step3.3
        stdDev += ((mean - income) ** 2)/numberOfEmployees
    stdDev = sqrt(stdDev)                                                                                           #Step3.4
   
    return stdDev                                                                                                   #Step3.5
    

#function computes medians of a set of numbers
def median( incomeList ) :                                                                                          #Step4
    numberOfEmployees = len(incomeList)                                                                             #Step4.1
    incomelist = sorted(incomeList)                                                                                 #Step4.2
    if numberOfEmployees % 2 == 0:                                                                                  #Step4.3
        median1 = incomelist[numberOfEmployees//2]
        median2 = incomelist[numberOfEmployees//2 - 1]
        median = (median1 + median2)/2
    else:                                                                                                           #Step4.4
        median = incomelist[numberOfEmployees//2]
  
    return median                                                                                                   #Step4.5

#Modes computations for a set of items in a list
def computeModes( incomeList ) :                                                                                    #Step5                                                                                #Step6.1
    dictionaryList = []                                                                                             #Step5.1
    dictionaries = {}                                                                                               #Step5.2
    max_count = 0                                                                                                   #Step5.3
    for income in incomeList:                                                                                       #Step5.4
        dictionaries[income] = dictionaries.get(income, 1) + 1                                                      #Step5.4.1
        if dictionaries[income] > max_count:                                                                        #Step5.4.2
            max_count = dictionaries[income]
    for income, dictionary in dictionaries.items():                                                                 #Step5.5
        if dictionary == max_count:                                                                                #Step5.5.1
            dictionaryList.append(income)

    return dictionaryList                                                                                           #Step6                                                                       