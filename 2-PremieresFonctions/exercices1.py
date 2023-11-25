def getUserInfo() :
    """Ask the user his name and age return the string 'Name: {name} - Age: {age}'"""


def fromFileToAnother() :
    """Ask the user a file path in and a file path out and create the file path out from the
    content of the file path in"""
    

def saveUserInformation() :
    """Ask the user his name and his age and save it in the file userInfo.txt
    in the format 'Name: {name} - Age: {age}'  
    after the other user information already present"""

def orderList(list) :
    """  
        Order the list from alphanumeric order [0-9][A-Z][a-z]
    
        Parameters
        ----------
        list : 
            A list to order
            
    """




if __name__ == '__main__':
    # Excercice 1
    print(getUserInfo())
    # Exercice 2
    fromFileToAnother()
    # Exercice 3
    saveUserInformation()
    # Exercice 4
    print(orderList(["1", "test","already", "Object"]))

