############# Pseudocode ##############
# Step1 - Define a function named 'computeProvTaxes' having variable 'income'
#   Step1.1 - If 'income' is greater than equal to 0 but less than equal to 29590.00, then
#             Set 'provtaxrate' equal to 0.0879.
#             Now compute 'provtaxinc' from the given formula: provtaxinc = provtaxrate * income
#   Step1.2 - Elif 'income' is greater than equal to 29590.01 but less than equal to 59180.00, then
#             Set 'provtaxrate' equal to 0.1495.
#             Now compute 'provtaxinc' from the given formula: provtaxinc = provtaxrate * (income - 29590.01) + 2600.96
#   Step1.3 - Elif 'income' is greater than equal to 59180.01 but less than equal to 93000:
#             Set 'provtaxrate' equal to 0.1667.
#             Now compute 'provtaxinc' from the given formula: provtaxinc = provtaxrate * (income - 59180.01) + 7024.70
#   Step1.4 - Elif 'income' is greater than equal to 93000.01 but less than equal to 150000.00, then
#             Set 'provtaxrate' equal to 0.1750.
#             Now compute 'provtaxinc' from the given formula: provtaxinc = provtaxrate * (income - 93000.01) + 12662.47 
#   Step1.5 - Else,
#             Set 'provtaxrate' equal to 0.21.
#             Now compute 'provtaxinc' from the given formula: provtaxinc = provtaxrate * (income - 150000.01) + 22637.47
#   Step1.6 - Return values of 'provtaxinc'.

# Step2 - Define a function named 'computeFedtaxes' from the variable 'income'
#   Step2.1 - If 'income' is greater than equal 0 to  but less than equal to 49020.00 , then
#             Set 'fedtaxrate' equal to 0.15.
#             Now compute 'fedtaxinc' from the given formula: fedtaxinc = fedtaxrate * income
#   Step2.2 - Elif 'income' is greater than equal to 49020.01 but less than equal to 98040.00 , then
#             Set 'fedtaxrate' equal to 0.2050.
#             Now compute 'fedtaxinc' from the given formula: fedtaxinc = fedtaxrate * (income - 49020.01) + 7353.00
#   Step2.3 - Elif 'income' is greater than equal to 98040.01 but less than equal to 151978.00:
#             Set 'fedtaxrate' equal to 0.26.
#             Now compute 'fedtaxinc' from the given formula: fedtaxinc = fedtaxrate * (income - 98040.01) + 17402.06
#   Step2.4 - Elif 'income' is greater than equal to  but less than equal to , then
#             Set 'fedtaxrate' equal to 0.29.
#             Now compute 'fedtaxinc' from the given formula: fedtaxinc = fedtaxrate * (income - 151978.01) + 31425.986 
#   Step2.5 - Else,
#             Set 'fedtaxrate' equal to 0.33.
#             Now compute 'fedtaxinc' from the given formula: fedtaxinc = fedtaxrate * (income - 216511.01) + 50140.57
#   Step2.6 - Return values of 'fedtaxinc'.

# Step3 - Define a function 'computeCPP' having a variable 'income'.
#   Step3.1 - Set 'cpprate' equal to 0.0525.
#   Step3.2 - Set 'employee_cppam' according to given formula: employee_cppam = income * cpprate
#   Step3.3 - If employee_cppam is greater than  2898.00, then
#             Set employee_cppam equal to 2898.00.
#   Step3.4 - Round the value of 'employee_cppam' equal to two decimal places.
#   Step3.5 - Return the values 'employee_cppam'.
 
# Step4 - Define a function 'computeEI' having a variable 'income'.
#   Step4.1 - Set 'EIrate' equal to 0.0525.
#   Step4.2 - Set 'employee_EI_am' according to given formula: employee_EI_am = income * EIrate
#   Step4.3 - If 'employee_EI_am' is greater than  856.36, then
#             Set 'employee_EI_am' equal to 856.36.
#   Step4.4 - Round the value of 'employee_EI_am' equal to two decimal places.
#   Step4.5 - Return the values 'employee_EI_am'.   

# Step5 - Define a function 'computeHealthPremium' having a variable 'income',
#   Step5.1 - If 'income' is less than equal to 22000.00, then
#               Set 'premium' equal to 0.00.
#   Step5.2 - Elif 'income' is greater than 22000.00 and  less than equal to 38000.00,
#             Compute 'result' according to given formula: result = 0.06 * (income - 22000.00)
#       Step5.2.1 - If result is less than 300.00, then
#                   'prmeium' is equal to 'result'.
#       Step5.2.2 - Else,
#                   premium = 300.00  
#   Step5.3 - Elif 'income' is greater than 38000.00 but less than equal to 50000.00, then
#             Compute 'result' according to given formula: result = 300 + 0.06 * (income - 38000.00)
#       Step5.3.1 - If 'result' is less than 450.00, then
#                   'premium' is equal to 'result'
#       Step5.3.2 - Else,
#                   'premium' is equal to 450.00.
#   Step5.4 - Elif 'income' is greater than 50000.00 but less than equal to 74000.00, then
#             Compute 'result' according to given formula: result = 450 + 0.25 * (income - 50000.00)
#       Step5.4.1 - If 'result' is less than 600.00, then
#                   'premium' is equal to 'result'.
#       Step5.4.2 - Else.
#                   'premium' is equal to 600.00.
#   Step5.5 - Elif 'income' is greater than 74000.00 but less than equal to 202000.00, then
#             Compute 'result' according to given formula: result = 600 + 0.25 * (income - 74000.00)
#       Step5.5.1 - If 'result' is less than 750.00, then
#                   'premium' is equal to 'result'.
#       Step5.5.2 - Else,
#                   premium is equal to 750.00
#   Step5.6 - Else,
#             Compute 'result' according to given formula: result = 750 + 0.25 * (income- 202000.00)
#       Step5.6.1 - If 'result' is less than 900.00:
#                   'premium' is equal to 'result'.
#       Step5.6.2 - Else,
#                   'premium' is equal to 900.00
#   Step5.7 - Return the values of 'premium'.

# Step6 - Define a function 'computeNetIncomes' having variable 'grossIncomeList',
#   Step6.1 - Set an empty list under tha name 'netIncomeList'.
#   Step6.2 - for 'grossIncome' in 'grossIncomeList',
#             Compute 'provtax' according to given formula: provtax = computeProvTaxes(grossIncome)
#             Compute 'fedtax' according to given formula: fedtax = computeFedTaxes(grossIncome) 
#             Compute 'employee_cpp' according to given formula: employee_cpp = computeCPP(grossIncome) 
#             Compute 'employee_EI' according to given formula: employee_EI = computeEI(grossIncome)
#             Compute 'premium' according to given formula: premium = computeHealthPremium(grossIncome)
#             Compute 'netincome' according to formula: netincome = round( grossIncome - (provtax + fedtax + employee_cpp + employee_EI + premium), 2)
#             Now append the values from 'netincome' into the 'netIncomeList'
#   Step6.3 - Return the 'netIncomeList'.



#operation computes provincial taxes for the input gross income...
def computeProvTaxes( income ) :                                                                                              #tep1
    
    if income >= 0 and income <= 29590.00:                                                                                    #Step1.1
        provtaxrate = 0.0879                                                                                                            
        provtaxinc = provtaxrate * income                                                                                         
    elif income >= 29590.01 and income <= 59180.00:                                                                           #Step1.2
        provtaxrate = 0.1495                                                                                                            
        provtaxinc = provtaxrate * (income - 29590.01) + 2600.96                                                       
    elif income >= 59180.01 and income <= 93000.00:                                                                           #Step1.3
        provtaxrate = 0.1667                                                                                                            
        provtaxinc = provtaxrate * (income - 59180.01) + 7024.70                                                      
    elif income >= 93000.01 and income <= 150000.00:                                                                          #Step1.4
        provtaxrate = 0.1750                                                                                                            
        provtaxinc = provtaxrate * (income - 93000.01) + 12662.47                                                      
    else:                                                                                                                     #Step1.5
        provtaxrate = 0.21                                                                                                                
        provtaxinc = provtaxrate * (income - 150000.01) + 22637.47                                                     

    return provtaxinc    

#operation computes federal taxes for the input gross income 
def computeFedTaxes( income ) :                                                                                               #Step2

    if income >= 0 and income <= 49020.00:                                                                                    #Step2.1
        fedtaxrate = 0.15                                                                                                               
        fedtaxinc = fedtaxrate * income                                                                                            
    elif income >= 49020.01 and income <= 98040.00:                                                                           #Step2.2
        fedtaxrate = 0.2050                                                                                                            
        fedtaxinc = fedtaxrate * (income - 49020.01) + 7353.00                                                         
    elif income >= 98040.01 and income <= 151978.00:                                                                          #Step2.3
        fedtaxrate = 0.26                                                                                                               
        fedtaxinc = fedtaxrate * (income - 98040.01) + 17402.06                                                        
    elif income >= 151978.01 and income <= 216511.00:                                                                         #Step2.4
        fedtaxrate = 0.29                                                                                                               
        fedtaxinc = fedtaxrate * (income - 151978.01) + 31425.986                                                       
    else:                                                                                                                     #Step2.5
        fedtaxrate = 0.33                                                                                                               
        fedtaxinc = fedtaxrate * (income - 216511.01) + 50140.57                                                       
                                                                                                
    return fedtaxinc
    
    
### Computing employee's CPP
def computeCPP( income ) :                                                                                                    #Step3
    cpprate = 0.0525                                                                                                          #Step3.1
    employee_cppam = income * cpprate                                                                                         #Step3.2
    if employee_cppam > 2898.00:                                                                                              #Step3.3
        employee_cppam = 2898.00  

    employee_cppam = round(employee_cppam, 2)                                                                                 #Step3.4
    return employee_cppam                                                                                                     #Step3.5  

### Computing employee's EI
def computeEI( income ) :                                                                                                     #Step4
  
    EIrate = 0.0158                                                                                                           #Step4.1
    employee_EI_am = income * EIrate                                                                                          #Step4.2
    if employee_EI_am > 856.36:                                                                                               #Step4.3
        employee_EI_am = 856.36                                                                                                         

    employee_EI_am = round(employee_EI_am, 2)                                                                                 #Step4.4
    return employee_EI_am                                                                                                     #Step5.5 
  
def computeHealthPremium( income ) :                                                                                          #Step5
    if income <= 22000.00:                                                                                                    #Step5.1
        premium = 0.00                                                                                                                  
    elif income > 22000.00 and income <= 38000.00:                                                                            #Step5.2
        result = 0.06 * (income - 22000.00)                                                                                   
        if result < 300:                                                                                                      #Step5.2.1
            premium = result                                                                                                           
        else:                                                                                                                 #Step5.2.2
            premium = 300.00                                                                                                            
    elif income > 38000.00 and income <= 50000.00:                                                                            #Step5.3
        result = 300 + 0.06 * (income - 38000.00)                                                                             
        if result < 450.00:                                                                                                   #Step5.3.1
            premium = result                                                                                                            
        else:                                                                                                                 #Step5.3.2
            premium = 450.00                                                                                                            
    elif income > 50000.00 and income <= 74000.00:                                                                            #Step5.4
        result = 450 + 0.25 * (income - 50000.00)                                                                             
        if result < 600.00:                                                                                                   #Step5.4.1
            premium = result                                                                                                            
        else:                                                                                                                 #Step5.4.2
            premium = 600.00                                                                                                            
    elif income > 74000.00 and income <= 202000.00:                                                                           #Step5.5
        result = 600 + 0.25 * (income - 74000.00)                                                                             
        if result < 750.00:                                                                                                   #Step5.5.1
            premium = result                                                                                                            
        else:                                                                                                                 #Step5.5.2
            premium = 750.00                                                                                                            
    else:                                                                                                                     #Step5.6
        result = 750 + 0.25 * (income- 202000.00)                                                                             
        if result < 900.00:                                                                                                   #Step5.6.1
            premium = result                                                                                                            
        else:                                                                                                                 #Step5.6.2
            premium = 900.00                                                                                                            
                                                                                                                 
    return premium                                                                                                            #Step5.7   

#Function computes net incomes by invoking
def computeNetIncomes( grossIncomeList ) :                                                                                    #Step6
    netIncomeList = []                                                                                                        #Step6.1
    for grossIncome in grossIncomeList:                                                                                       #Step6.2
        provtax = computeProvTaxes(grossIncome)                                                                               
        fedtax = computeFedTaxes(grossIncome)                                                                                 
        employee_cpp = computeCPP(grossIncome)                                                                                
        employee_EI = computeEI(grossIncome)                                                                                  
        premium = computeHealthPremium(grossIncome) 
                                                                                            
        netincome = round( grossIncome - (provtax + fedtax + employee_cpp + employee_EI + premium), 2)                       
        netIncomeList.append(netincome)                                                                                       
    
    return netIncomeList                                                                                                      #Step6.3s