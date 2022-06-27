############ Pseudocode #############
# Step1 - From skeleton import generateJSON, extractEmployeeInfo, extractGrossIncomes
# Step2 - From taxUtilities import everything
# Step3 - From statistics1 import mean, standardDeviation, median, ComputeModes
# Step4 - From time import time
# Step5 - From qualityAssurance import gradeAssignment
# Step6 - Define a function '_main_' 
#   Step6.1 - Set fileName equal to 'salaries'.
#   Step6.2 - Set extension equal to 'xls'
#   Step6.3 - From the 'skeleton.py' file write a function 'generateJSON' having variable from Step6.1, Step6.2 and 'number of sheets', in order to open the 'salaries.xls' through JSON.
#   Step6.4 - Set 'grossIncomeList' equal to function taken from 'skeleton.py' which is extractGrossIncomes having variable as 'fileName' and 'json'.
#   Step6.5 - Set 'netIncomeList' equal to function taken from 'utilities.py' which is 'computeNetIncomes' having variable as 'grossIncomeList'.
#   Step6.6 - Set 'averageGrossIncomes' equal to function taken from 'statisitcs1.py' which is 'mean' having variable as 'grossIncomeList'.
#   Step6.7 - Set 'averageNetIncomes' equal to function taken from 'statistics.py' which is 'mean' having variable as 'netIncomeList'.
#   Step6.8 - Now print the value of average of gross income of the employees from step6.6 and format the value to two decimal places.
#   Step6.9 - Now print the value of average of net incomes of the employees form step6.7 and format the value to two decimal places.
#   Step6.10 - Now print the average of all modes of the employees using the 'mean' function on the another function 'computeModes' both taken from 'statistics.py' having variable ' netIncomeList' and format the value to only two decimal places.
#   Step6.11 - Now print the variance for employees by using the standardDeviation' function taken from 'statistics.py' having variables as 'netIncomeList' and 'averageNetIncomes' and whole square the value found  and then format the value to two decimal places.
#   Step6.12 - Now print the Median for emplyees by using the 'median' function taken from 'statisitcs.py' having variable as 'netIncomeList' and format the values to two decimal places.
#   Step6.13 - Write the function 'gradeAssignment()' taken from 'qualityAssurance.py'
# Step7 - Write variable 'start' equal to 'time()' funciton from Step4.
# Step8 - Write the '_main_' funciton from Step6.
# Step9 - Print the time of execution by using step7.
# Step10 - Stop

from Gurkanwaljot_Brar_300183144_skeleton import generateJSON, extractEmployeeInfo, extractGrossIncomes                         #Step1
from Gurkanwaljot_Brar_300183144_taxutilities import *                                                                          #Step2
from Gurkanwaljot_Brar_300183144_statistics1 import mean, standardDeviation, median, computeModes                               #Step3
from time import time                                                                               #Step4
from Gurkanwaljot_Brar_300183144_qualityAssurance import gradeAssignment                                                        #Step5


    #defines the entry point logic of the entire program
def _main_() :                                                                                      #Step6

    fileName = 'salaries'                                                                           #Step6.1
    extension = 'xls'                                                                               #Step6.2

    #generating the JSON equaivalent of the excel sheet
    generateJSON( fileName, extension, 0, 0, 0, 1 )                                                 #Step6.3
    grossIncomeList = extractGrossIncomes ( fileName, 'json' )                                      #Step6.4
    netIncomeList = computeNetIncomes( grossIncomeList )                                            #Step6.5
    averageGrossIncomes = mean( grossIncomeList )                                                   #Step6.6    
    averageNetIncomes = mean( netIncomeList )                                                       #Step6.7

    print( "\n************* Required Information ************* \n" )                                
    print( f"Average gross-income for Nova Scotia's employees: $(CAD) {format( averageGrossIncomes, ',.2f' )}" )            #Step6.8
    print( f"Average net-income for Nova Scotia's employees: $(CAD) {format( averageNetIncomes, ',.2f' )}" )                #Step6.9
    print( f"Average of all modes for Nova Scotia's employees: $(CAD) {format( mean( computeModes( netIncomeList ) ), ',.2f' )}" )          #Step6.10
    print( f"Population variance for Nova Scotia's employees: $(CAD) {format( standardDeviation( netIncomeList, averageNetIncomes ) ** 2, ',.2f' )}" )              #Step6.11
    print( f"Median for Nova Scotia's employees: $(CAD) {format( median( netIncomeList ), ',.2f' )}" )                      #Step6.12
  
    gradeAssignment()                                                                               #Step6.13
#setting up a time watcher to monitor execution time
start = time()                                                                                      #Step7
#invoking the main function
_main_()                                                                                            #Step8
print(f"Time taken for execution: {format(time() - start, '.2f')} seconds.")                        #Step9