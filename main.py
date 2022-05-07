from os import remove
from tkinter import *
from numpy import load
from tkinter.ttk import Combobox
from os.path import exists
import datetime
from Pet import Pet


root = Tk()
root.title('Tamagotchi')
root.resizable(width=False, height=False)

canv = Canvas(root, width=750, height=600, bg="white")
canv.grid()


pet = None


def Loop():
    global pet
    if pet.hasRun:

        if pet.hasRun:
            sorry_text = canv.create_text(
                375, 250, justify=CENTER,
                text="I'm sorry!\nYour pet has run away,\nbecause you"
                     "didn't care enough of it",
                     font=("Courier", 22, "bold"))

            def again():
                remove("./data.npy")
                canv.delete(sorry_text)
                again_button.destroy()
                pet.isDead = False
                main()

            again_button = Button(
                root, text="Get another pet(((", command=lambda: again(),
                           font=("Courier", 18), bg="light blue")
            again_button.place(x=225, y=400, width=300, height=60)

        return
    else:
        pet.update_all()
        root.after(1000, Loop)


def main():
    global pet
    if exists("./data.npy"):
        datas = load("./data.npy", allow_pickle=True)
        pet = Pet(datas[0], datas[1], datas[2], datas[3], datas[4],
                  datas[5], datas[6], datas[7], datas[8], canv, root)

        cur_date = datetime.datetime.today()
        difference = cur_date - datas[9]
        actual_difference = difference.seconds + 86400 * difference.days

        pet.update_food(-0.001 * actual_difference)
        pet.update_health(-0.001 * actual_difference)
        pet.update_joy(-0.001 * actual_difference)
        pet.age += actual_difference
        pet.timeToPoop -= actual_difference
        if pet.timeToPoop < 0:
            pet.timeToPoop = 0

        pet.update_all()
        Loop()

    else:

        pet_type = None
        pet_name = None

        choose_text = canv.create_text(360, 100, text="Choose your pet:",
                                       font=("Courier", 22, "bold"))
        type_text = canv.create_text(200, 200, text="Choose type:",
                                     font=("Courier", 20, "bold"))
        name_text = canv.create_text(550, 200, text="Choose name:",
                                     font=("Courier", 20, "bold"))

        def agree():
            global pet
            nonlocal pet_type
            nonlocal pet_name
            pet_type = choose_type.get()
            pet_name = choose_name.get()
            pet = Pet(pet_type, pet_name, 0, 100, 100, 100,
                      False, 60, [], canv, root)
            agree_button.destroy()
            choose_type.destroy()
            choose_name.destroy()
            canv.delete(name_text)
            canv.delete(type_text)
            canv.delete(choose_text)
            Loop()

        cur_font = ("Arial", 18)
        root.option_add("*TCombobox*Listbox*Font", cur_font)
        choose_type = Combobox(root, state="readonly", font=cur_font)
        choose_type["values"] = (
            "cat", "horse", "pig", "dog", "hen", "turtle", "rabbit",
            "koala", "elephant", "beagle", "lion", "panda",
            "penguin", "whale", "sheep")
        choose_type.place(x=100, y=250, width=200, height=40)

        agree_button = Button(root, text="I choose you!",
                              font=cur_font, bg="pink",
                              command=lambda: agree())
        agree_button.place(x=250, y=400, width=200, height=50)

        choose_name = Entry(root, font=18, bd=5)
        choose_name.place(x=450, y=250, width=200, height=40)


main()
root.mainloop()
