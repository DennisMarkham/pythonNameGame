import re

def play():
    name = input("Enter name:")

    num = 2

#checks if second letter is vowel.  This when "Steven" becomes "Beven" not
#"Bteven" but "Sarah" still becomes "Barah"
    
    x = re.search(r"[aeiou]", name[1])

    if x:
     num = 1


    print(name + " bo " + name.replace(name[0:num], "B") + " banana fanna fo " +
          name.replace(name[0:num], "F") + " " + name)

#looping
    play()

play()
