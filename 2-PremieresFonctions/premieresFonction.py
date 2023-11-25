def returnTheVariable() :
    return "result"

def modify(entry) :
    entry = "newResult"

def modifyList(entry : list) :
    entry[0] = 2

if __name__ == '__main__':
    temp = 1+1
    print('2 = ', temp)
    temp = "String"
    print(temp)
    temp = b"s"
    print("plurials is done with char ", temp)
    print(temp.__class__)
    temp = returnTheVariable
    print("temp is a function ", temp)
    temp = returnTheVariable()
    print("temp is a string ", temp)
    modify(temp)
    print("temp is not modified so always ", temp)
    temp = [0]
    print("temp is a list : ", temp)
    modifyList(temp)
    print("temp is updated because he is not reassigned ", temp)