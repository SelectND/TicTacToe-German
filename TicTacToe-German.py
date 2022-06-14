

def printField(field):
    print(f"{field[0]} | {field[1]} | {field[2]}")
    print(f"{field[3]} | {field[4]} | {field[5]}")
    print(f"{field[6]} | {field[7]} | {field[8]}")
    
def setPoint(xo, field):
    while True:
        where = input(f"Wo möchtest du, {xo}, dein Zeichen setzen? ")
        try:
            where = int(where)-1
        except:
            print("Das Eingegebene ist keine gültige Zahl! Bitte erneut versuchen")
            continue
        if field[where] != " ":
            print("Das Feld ist schon besetzt! Bitte gebe eine andere Zahl ein.")
            continue
        elif field[where] == " ":
            field[where] = xo
            print("Zeichen wurde gesetzt. Der nächste, bitte!")
            break
        else:
            print("Es ist ein Fehler aufgetreten! Bitte versuche es erneut.")
            continue
    return field

def checkWinOrTie(field):
    emptyPlates = 9
    for plate in field:
        if(plate != " "):
            emptyPlates -= 1
    if emptyPlates == 0:
        return "tie"
    
    
    if(field[0] == "X" and  field[1] == "X" and  field[2] == "X"):
        return "X"
    elif(field[3] == "X" and  field[4] == "X" and  field[5] == "X"):
        return "X"
    elif(field[6] == "X" and  field[7] == "X" and  field[8] == "X"):
        return "X"
    elif(field[0] == "X" and  field[3] == "X" and  field[6] == "X"):
        return "X"
    elif(field[1] == "X" and  field[4] == "X" and  field[7] == "X"):
        return "X"
    elif(field[2] == "X" and  field[5] == "X" and  field[8] == "X"):
        return "X"
    elif(field[0] == "X" and  field[4] == "X" and  field[8] == "X"):
        return "X"
    elif(field[2] == "X" and  field[4] == "X" and  field[6] == "X"):
        return "X"
        
    if(field[0] == "O" and  field[1] == "O" and  field[2] == "O"):
        return "O"
    elif(field[3] == "O" and  field[4] == "O" and  field[5] == "O"):
        return "O"
    elif(field[6] == "O" and  field[7] == "O" and  field[8] == "O"):
        return "O"
    elif(field[0] == "O" and  field[3] == "O" and  field[6] == "O"):
        return "O"
    elif(field[1] == "O" and  field[4] == "O" and  field[7] == "O"):
        return "O"
    elif(field[2] == "O" and  field[5] == "O" and  field[8] == "O"):
        return "O"
    elif(field[0] == "O" and  field[4] == "O" and  field[8] == "O"):
        return "O"
    elif(field[2] == "O" and  field[4] == "O" and  field[6] == "O"):
        return "O"
    else:
        return "non"

if __name__ == "__main__":
    xoIndex = 0
    win = "non"
    field = [" "," "," "," "," "," "," "," "," "]
    while win == "non":
        printField(field)
        if(xoIndex == 0):
            newField = setPoint("X", field)
            xoIndex += 1
        elif(xoIndex == 1):
            newField = setPoint("O", field)
            xoIndex -= 1
        else:
            print("Internal Error at setpoint change!")
        field = newField
        win = checkWinOrTie(field)
        
    if win == "tie":
        print("Das Spiel endete unentschieden.")
    else:
        printField(field)
        print(f"Juuhuuu! {win} hat gewonnen! Herzlichen Glückwunsch")
    
    