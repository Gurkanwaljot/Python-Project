from Gurkanwaljot_Brar_300183144_testcases import *

def points( index ) :
		
	#returns approriate grade points based on the test index
    x = 5
    if( index == 0 ) :
        return 2 * 0.5 
    elif( index == 1 ) : 
        return 2 * 0.5
    elif( index == 2 ) :
        return 1 * 1 
    elif( index == 3 ) :
        return 1 * 1
    elif( index == 4 ) :
        return 2 * 0.5
    elif( index == 5 ) :
        return 1 * 1
    elif( index == 6 ) :
        return 1 * 1
    elif( index == 7 ) :
        return 4 * x - 3
    elif( index == 8 ) :
        return 1 * x
    elif( index == 9 ) :
        return 5 * x - 4
    else :
        return 0
        
def test() :
    
    test = []
    test.append( evaluateQuestion( q1() ) )
    test.append( evaluateQuestion( q2() ) )
    test.append( evaluateQuestion( q3() ) )
    test.append( evaluateQuestion( q4() ) )
    test.append( evaluateQuestion( q5() ) )
    test.append( evaluateQuestion( q6() ) )
    test.append( evaluateQuestion( q7() ) )
    test.append( evaluateQuestion( q8() ) )
    test.append( evaluateQuestion( q9() ) )
    test.append( evaluateQuestion( q10() ) )
    
    return test

#this method computes students grade for this lab...
def gradeAssignment() :

    flag = True
    totalPoints = 0
    i = 0
    
    print("\n//...Running testcases for the operations...//")
    myTest = test() #invoking the test(...) method
    while( i < len( myTest ) ) :
    
        myPoints = format( points( i ), '.2f' )
        if( myTest[i] == True ) :
            print(f"Test {i}, Q{i+1} passed. [Alloted point(s): {myPoints}]")
            totalPoints += points( i )
        else :
            print(f"Test {i} Q{i+1} failed. [Alloted point(s): {myPoints}]")
            flag = False
            
        i += 1
    
    if( flag ) :
        print("All tests are successful.")
    else :
        print("Not all tests are successful.")
    
    print(f"Total points earned in this assignment: {format(totalPoints, '.2f')} points")
    print("//..............End..........................//")