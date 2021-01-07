import sys
ISBN = input('Enter a ISBN: ')
isbn = {'0','1','2','3','4','5','6','7','8','9','10','X','.'}
list2 = list(ISBN)

def controlNumberCheck():    
    list1 = list(ISBN)
    if '.' in list1:
        list1 = list2
    else:
        list1 = list1
    multiply_list = [10,9,8,7,6,5,4,3,2]
    controlNumber = 0
    for c in range(0,9):        
        multiply = float(multiply_list[c]) * float(list1[c])
        controlNumber = float(controlNumber) + float(multiply)
    return float(controlNumber)


def checkDigitF():       
    checkDigit =  list2[-1]
    if checkDigit == 'X':
        checkDigit = 10
    elif checkDigit == 10:
        print('X')
        sys.exit()
    return int(checkDigit)
    
def Test():
    test = (controlNumberCheck() + checkDigitF()) % 11      
    if test == 0 :
        return True
    else:
        return False

def pointCheck():    
    for i in range (len(list2)):
        if list2[i] == '.':
            for x in range(0,11):
                    list2[i] = x
                    if Test() == True:
                        print(x)
                        sys.exit()                       
    return(list2[x])     

if not isbn.issuperset(ISBN) or len(ISBN) >= 11 or len(ISBN) < 10:
    print('INPUT ERROR')
    sys.exit()
else:
    if '.' in list(ISBN):
        pointCheck()
    else:
        if Test() == True:
            print('VALID')
        else:
            print('INVALID') 
print()
