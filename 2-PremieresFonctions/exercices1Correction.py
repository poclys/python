def getUserInfo() :
    """Ask the user his name and age return the string 'Name: {name} - Age: {age}'"""
    name = input("Votre nom : ")
    age = input("Votre age : ")
    return "Name: " + name + " - Age: " + str(int(age))

def fromFileToAnother() :
    """Ask the user a file path in and a file path out and create the file path out from the
    content of the file path in"""
    filePathIn = input("Votre fichier à copier : ")
    filePathOut = input("Le fichier cible : ")
    with open(filePathIn, "r") as filin:
        with open(filePathOut, "w") as filout:
            lignes = filin.readlines()
            #filout.writelines(lignes)
            for ligne in lignes:
                filout.write(ligne)

def saveUserInformation() :
    """Ask the user his name and his age and save it in the file userInfo.txt
    in the format 'Name: {name} - Age: {age}'  
    after the other user information already present"""
    toSave = getUserInfo()
    with open("userInfo.txt", "a") as filout:
        filout.write(toSave + "\n")



def orderList(list) :
    """  
        Order the list from alphanumeric order [0-9][A-Z][a-z]
    
        Parameters
        ----------
        list : 
            A list to order
            
    """
    #list.sort()
    for a in range(len(list)) :
        for b in range(len(list)) :
            if list[a] < list[b] :
                tmp = list[a]
                list[a] = list[b]
                list[b] = tmp
    return list



if __name__ == '__main__':
    # Excercice 1
    #print(getUserInfo())
    # Exercice 2
    #fromFileToAnother()
    # Exercice 3
    #saveUserInformation()
    # Exercice 4
    print(orderList(["1", "test","already", "Object"]))

