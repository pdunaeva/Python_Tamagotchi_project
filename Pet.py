import tkinter

from tkinter import *
import tkinter.font
import random
from numpy import save
import datetime

AnimalBitmaps = {
    "cat": '0000000000000000000000000000000000000000000000001110000'
           '0111000111001111100100011101000001010001101010001010011'
           '0101010001011110100100010001000100001010101000001000011'
           '1111010001000010001001110100010011001101010001110111001'
           '110000000000000000000000000000000000',
    "horse": '00000000000000000000000000000000000000000000000000001'
             '11100000000000111011000000001100011100000001001001111'
             '00111010000001111111110111000000000111000010010000001'
             '10000110100100111000101011110101100010101010110100001'
             '10110111011000000000000000000000000000000000',
    "pig": '0000000000000000000000000000000000000000000000000000110'
           '0110000000001011101000000001000000011001000110011100010'
           '0101111001000001011000010000000101110101000000001010000'
           '1000010001001111001010000100001011101100100000110011001'
           '100000000000000000000000000000000000',
    "dog": "0000000000000000000000000000000000000000000000000000110"
           "0111000000001011100100000001000001100111000110100010010"
           "1111100000010001011100000100111101100001100000001101111"
           "0000010001000010110010100100010110010100100001110111111"
           "100000000000000000000000000000000000",
    "hen": "0000000000000000000000000000000000000000000000000111100"
           "0000000000111110000000000010001000000000011010100000110"
           "0011100101111101000001001000100100000100011100100000001"
           "0000001000000000111111000000000001001000000000001101100"
           "000000000000000000000000000000000000",
    "turtle": "0000000000000000000000000000000000000000000000000000"
              "0000000000000000000000000000001100011111000001001010"
              "1010100010101111111111001000101010101010011001111111"
              "1110000101101010101000001111111111110000010010100100"
              "000001110001110000000000000000000000000000000000",
    "rabbit": "0000000000000000000000000000000000000000000000000000"
              "11111100000000010000100000000010011111100000010110000"
              "10000001000001110011000101001111110010010000100000101"
              "00110000000000100001000010110010000100011100010000011"
              "110011110000000000000000000000000000000000000",
    "koala": "000000000000000000000000000000000000000000000000111100"
             "000011110001001111110010001101000001001100011010010011"
             "000000100000001001100010110000111001000111000100010100"
             "001111100000100001000000110010000100100101001000001101"
             "1110110000000000000000000000000000000000",
    "elephant": "000000000000000000000000000000000000000000000000000"
                "111100000000000100001100000000100001001110000010010"
                "000100100010000010010001001000101001000100100101011"
                "000010010101000000001001011010101010100100101010101"
                "0100011001101011100000000000000000000000000000000000",
    "beagle": "00000000000000000000000000000000000000000000000000111"
              "00000000000010001100000011001010001000010101000010010"
              "01010011000100111110001000101110001000011100000000100"
              "00010100111010100010111010101010001110110011011000000"
              "00000000000000000000000000000000000000000000",
    "lion": "0000000000000000000000000000000000000000000000000010111"
            "0000000000111111110000000111111111100011011100011100001"
            "1010110110110000111101010111111001110000011100110111101"
            "0111000011001111111101101000011111101110100000111011101"
            "110000000000000000000000000000000000",
    "panda": "000000000000000000000000000000000000000000000000011000"
             "001100000011111111111000001110000011100000010110110100"
             "011001011011010001100100010001111110001000001110000101"
             "111111111001110110000111001111111111111111111111100111"
             "0011110000000000000000000000000000000000",
    "penguin": "0000000000000000000000000000000000000000000000000000"
               "1111100000000001100011000000000100101100000000111000"
               "1110000001111001111000000001000011111000001100000111"
               "1100011100000011111000011000001100000000111111110000"
               "001111001110000000000000000000000000000000000000",
    "whale": "000000000000000000000000000000000000000000000000001101"
             "100011001001001001001111110000100000011111001111100000"
             "111001111111100011101110111111011110111111111111111011"
             "111111111111001111110111111100011111100011100000111111"
             "1111000000000000000000000000000000000000",
    "sheep": "000000000000000000000000000000000000000000000000000011"
             "011100000000110010001101100111100000001001111101000000"
             "010111011100000001101111000000000100111000000000010000"
             "101001010010000011111111111000001101101111000000000000"
             "000000000000000000000000"}

poop_bitmap = "01001001100100100100100110000010000110000011110001111" \
              "11011111111"


def time_to_str(time):
    sec = time % 60
    time //= 60
    minutes = time % 60
    time //= 60
    hour = time % 24
    time //= 24
    answer = str(time) + " days, " + str(hour) + " hours, " \
        + str(minutes) + " min, " + str(sec) + " sec"
    return answer


class Pet:
    def __init__(self, type, name, age, food, health, joy,
                 is_poop, time_to_poop, words, canv, root):
        self.canv = canv
        self.root = root
        self.type = type
        self.name = name
        self.age = age
        self.health = health
        self.food = food
        self.joy = joy
        self.isPoop = is_poop
        self.timeToPoop = time_to_poop
        self.words = words
        self.current_word = ""

        if len(self.words) == 0:
            self.words.append("Hello!")
            self.words.append("Nice to meet you!")

        self.hasRun = False
        self.poop_picture = []
        self.picture = []

        # draw pet

        x = 0
        y = 0
        for i in range(len(AnimalBitmaps[self.type])):
            pix = AnimalBitmaps[self.type][i]
            if pix == "1":
                self.picture.append(
                    canv.create_rectangle(
                        60 + x, 130 + y, 60 + x + 15, 130 + y + 15,
                        fill="black"))
            x += 15
            if x == 240:
                x = 0
                y += 15

        if self.isPoop:
            global poop_bitmap
            x = 0
            y = 0
            for i in range(64):
                sym = poop_bitmap[i]
                if sym == "1":
                    self.poop_picture.append(
                        canv.create_rectangle(310 + x, 300 + y,
                                              310 + x + 5, 300 + y + 5,
                                              fill='brown', outline='brown'))
                x += 5
                if x == 40:
                    x = 0
                    y += 5

        # add texts

        self.name_text = canv.create_text(
            180, 100, text=self.name,
            font=tkinter.font.Font(family='Helvetica', size=20))
        self.age_text = canv.create_text(
            375, 35, text="Your pet is " + time_to_str(self.age) + " old!",
            font=tkinter.font.Font(family='Helvetica', size=16))

        # add stats

        self.food_bar_border = canv.create_rectangle(
            430, 100, 480, 300, outline="red")
        self.health_bar_border = canv.create_rectangle(
            530, 100, 580, 300, outline="green")
        self.joy_bar_border = canv.create_rectangle(
            630, 100, 680, 300, outline="purple")

        self.food_bar = canv.create_rectangle(
            430, 100 + 200 - 2 * self.food, 480, 300,
            fill="red", outline="red")
        self.health_bar = canv.create_rectangle(
            530, 100 + 200 - 2 * self.health, 580, 300,
            fill="green", outline="green")
        self.joy_bar = canv.create_rectangle(
            630, 100 + 200 - 2 * self.joy, 680, 300,
            fill="purple", outline="purple")

        self.food_title = canv.create_text(
            455, 320, text="FOOD", fill="red",
            font=tkinter.font.Font(size=16))
        self.health_title = canv.create_text(
            555, 320, text="HEALTH", fill="green",
            font=tkinter.font.Font(size=16))
        self.joy_title = canv.create_text(
            655, 320, text="JOY", fill="purple",
            font=tkinter.font.Font(size=16))

        self.food_text = canv.create_text(
            455, 340, text=str(self.food) + "%",
            fill="red", font=tkinter.font.Font(size=16))
        self.health_text = canv.create_text(
            555, 340, text=str(self.health) + "%",
            fill="green", font=tkinter.font.Font(size=16))
        self.joy_text = canv.create_text(
            655, 340, text=str(self.joy) + "%",
            fill="purple", font=tkinter.font.Font(size=16))

        self.current_word = random.choice(self.words)
        self.phrase = canv.create_text(
            180, 450, text=self.current_word,
            font=tkinter.font.Font(size=18))

        self.pet_says = canv.create_text(
            180, 400, text="Your pet says:",
            font=tkinter.font.Font(size=18))

        self.feed_button = Button(
            root, text="Feed", background="red", font=16,
            command=lambda: self.update_food(5))
        self.feed_button.place(x=410, y=380, height=60, width=90)

        self.heal_button = Button(
            root, text="Heal", background="green", font=16,
            command=lambda: self.update_health(5))
        self.heal_button.place(x=510, y=380, height=60, width=90)

        self.play_button = Button(
            root, text="Play", background="purple", font=16,
            command=lambda: self.update_joy(5))
        self.play_button.place(x=610, y=380, height=60, width=90)

        self.clean_button = Button(
            root, text="Clean", background="yellow", font=16,
            command=lambda: self.clean())
        self.clean_button.place(x=410, y=450, height=60, width=90)

        self.talk_button = Button(
            root, text="Talk", background="light blue", font=16,
            command=lambda: self.talk())
        self.talk_button.place(x=510, y=450, height=60, width=90)

        self.teach_button = Button(
            root, text="Teach", background="pink", font=16,
            command=lambda: self.word_choice())
        self.teach_button.place(x=610, y=450, height=60, width=90)

    def save(self):
        datas = [self.type, self.name, self.age,
                 self.food, self.health, self.joy,
                 self.isPoop, self.timeToPoop,
                 self.words, datetime.datetime.today()]
        save("./data.npy", datas)

    def run_away(self):
        self.hasRun = True
        self.canv.delete(self.food_bar)
        self.canv.delete(self.health_bar)
        self.canv.delete(self.joy_bar)
        self.canv.delete(self.food_text)
        self.canv.delete(self.health_text)
        self.canv.delete(self.joy_text)
        self.canv.delete(self.phrase)
        self.canv.delete(self.pet_says)
        self.feed_button.destroy()
        self.play_button.destroy()
        self.heal_button.destroy()
        self.teach_button.destroy()
        self.clean_button.destroy()
        self.talk_button.destroy()
        self.canv.delete(self.age_text, self.name_text, self.health_bar_border,
                         self.food_bar_border, self.joy_bar_border,
                         self.joy_title, self.food_title, self.health_title)

        for pix in self.picture:
            self.canv.delete(pix)

        if self.isPoop:
            for pix in self.poop_picture:
                self.canv.delete(pix)

    def update_states(self):
        self.canv.delete(self.food_bar)
        self.canv.delete(self.health_bar)
        self.canv.delete(self.joy_bar)
        self.food_bar = self.canv.create_rectangle(
            430, 100 + 200 - 2 * self.food, 480, 300,
            fill="red", outline="red")
        self.health_bar = self.canv.create_rectangle(
            530, 100 + 200 - 2 * self.health, 580, 300,
            fill="green", outline="green")
        self.joy_bar = self.canv.create_rectangle(
            630, 100 + 200 - 2 * self.joy, 680, 300,
            fill="purple", outline="purple")

        self.canv.delete(self.food_text)
        self.canv.delete(self.health_text)
        self.canv.delete(self.joy_text)
        self.food_text = self.canv.create_text(
            455, 340, text=str(round(self.food, 2)) + "%", fill="red",
            font=tkinter.font.Font(size=16))
        self.health_text = self.canv.create_text(
            555, 340, text=str(round(self.health, 2)) + "%", fill="green",
            font=tkinter.font.Font(size=16))
        self.joy_text = self.canv.create_text(
            655, 340, text=str(round(self.joy, 2)) + "%", fill="purple",
            font=tkinter.font.Font(size=16))

    def update_food(self, n):
        self.food += n
        if self.food > 100:
            self.food = 100
        elif self.food < 0:
            self.food = 0
            self.update_health(-0.007)
            self.update_joy(-0.01)

    def update_joy(self, n):
        self.joy += n
        if self.joy > 100:
            self.joy = 100
        elif self.joy < 0:
            self.joy = 0
            self.update_health(-0.005)

    def update_health(self, n):
        self.health += n
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0
            self.hasRun = True

    def get_food(self):
        self.update_food(5)

    def get_pills(self):
        self.update_health(5)

    def play(self):
        self.update_joy(5)

    def learn_new_word(self, word, enter_window):
        self.words.append(word)
        self.update_joy(7)
        enter_window.destroy()

    def word_choice(self):
        enter_window = tkinter.Toplevel(self.root)
        enter_window.geometry('300x120')
        new_word = Entry(enter_window, width=200, font=18, bd=5)
        enter_but = Button(enter_window, text="Ok", bd=5, font=18,
                           command=lambda: self.learn_new_word(
                               new_word.get(), enter_window))
        enter_but.place(x=120, y=60, width=60, height=40)
        new_word.pack()

    def talk(self):
        old_phrase = self.current_word
        while self.current_word == old_phrase:
            self.current_word = random.choice(self.words)
        self.canv.delete(self.phrase)
        self.phrase = self.canv.create_text(180, 450, text=self.current_word,
                                            font=tkinter.font.Font(size=18))

    def poop(self):
        if self.isPoop:
            self.update_health(-1)
            self.update_joy(-1)
            self.timeToPoop = 21600
            pass
        self.isPoop = True
        self.timeToPoop = 21600
        # draw poop
        global poop_bitmap
        x = 0
        y = 0
        for i in range(64):
            sym = poop_bitmap[i]
            if sym == "1":
                self.poop_picture.append(
                    self.canv.create_rectangle(310 + x, 300 + y,
                                               310 + x + 5, 300 + y + 5,
                                               fill='brown', outline='brown'))
            x += 5
            if x == 40:
                x = 0
                y += 5

    def clean(self):
        if not self.isPoop:
            return
        self.update_joy(2)
        self.isPoop = False
        for pix in self.poop_picture:
            self.canv.delete(pix)

    def update_all(self):
        if self.hasRun:
            self.run_away()
        self.update_food(-0.001)
        self.update_health(-0.001)
        self.update_joy(-0.001)
        self.timeToPoop -= 1
        if self.timeToPoop <= 0:
            self.poop()
        self.age += 1

        self.canv.delete(self.age_text)
        self.age_text = self.canv.create_text(
            375, 35, text="Your pet is " + time_to_str(self.age) + " old!",
            font=tkinter.font.Font(family='Helvetica', size=16))

        self.update_states()

        if self.timeToPoop == 0:
            self.poop()

        self.save()

        if self.hasRun:
            self.run_away()
