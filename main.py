import lotteri
import os

lotteriet = lotteri.Lotteri()

looping = True

while looping:

    os.system("cls" if os.name == "nt" else "clear")

    antal_lotter = input("\n\t\tHur många lotter vill du ha? OBS max 3! ")

    try:
        int_antal_lotter = int(antal_lotter)
        i = 0
        if(int_antal_lotter <=3):
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\t\tStort GRATTIS! Du vann det här:")
            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print("\t\t" + vinst)
                i+=1

        elif(int_antal_lotter > 3):
            print("\n\t\tDu har valt för många lotter >:(")

    except ValueError:
        print("\n\t\tError")

    print("-----------------------------------")
    spela_igen = input("\n\t\n\tVill du spela igen? j/n ")
    if (spela_igen == "n"):
        break

