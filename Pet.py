import tkinter

from tkinter import *
import tkinter.font
import random
from numpy import save
import datetime


AnimalBitmaps = {
    "cat": '0000000000000000000000000000000000000000000000001110000011100011100111110010001110100000101000110101000101001101010100010111101001000100010001000010101010000010000111111010001000010001001110100010011001101010001110111001110000000000000000000000000000000000',
    "horse": '0000000000000000000000000000000000000000000000000000111100000000000111011000000001100011100000001001001111001110100000011111111101110000000001110000100100000011000011010010011100010101111010110001010101011010000110110111011000000000000000000000000000000000',
    "pig": '0000000000000000000000000000000000000000000000000000110011000000000101110100000000100000001100100011001110001001011110010000010110000100000001011101010000000010100001000010001001111001010000100001011101100100000110011001100000000000000000000000000000000000',
    "dog": "0000000000000000000000000000000000000000000000000000110011100000000101110010000000100000110011100011010001001011111000000100010111000001001111011000011000000011011110000010001000010110010100100010110010100100001110111111100000000000000000000000000000000000",
    "hen": "0000000000000000000000000000000000000000000000000111100000000000011111000000000001000100000000001101010000011000111001011111010000010010001001000001000111001000000010000001000000000111111000000000001001000000000001101100000000000000000000000000000000000000",
    "turtle": "0000000000000000000000000000000000000000000000000000000000000000000000000000000000110001111100000100101010101000101011111111110010001010101010100110011111111110000101101010101000001111111111110000010010100100000001110001110000000000000000000000000000000000",
    "rabbit": "0000000000000000000000000000000000000000000000000000111111000000000100001000000000100111111000000101100001000000100000111001100010100111111001001000010000010100110000000000100001000010110010000100011100010000011110011110000000000000000000000000000000000000",
    "koala": "0000000000000000000000000000000000000000000000001111000000111100010011111100100011010000010011000110100100110000001000000010011000101100001110010001110001000101000011111000001000010000001100100001001001010010000011011110110000000000000000000000000000000000",
    "elephant": "0000000000000000000000000000000000000000000000000001111000000000001000011000000001000010011100000100100001001000100000100100010010001010010001001001010110000100101010000000010010110101010101001001010101010100011001101011100000000000000000000000000000000000",
    "beagle": "0000000000000000000000000000000000000000000000000011100000000000010001100000011001010001000010101000010010010100110001001111100010001011100010000111000000001000001010011101010001011101010101000111011001101100000000000000000000000000000000000000000000000000",
    "lion": "0000000000000000000000000000000000000000000000000010111000000000011111111000000011111111110001101110001110000110101101101100001111010101111110011100000111001101111010111000011001111111101101000011111101110100000111011101110000000000000000000000000000000000",
    "panda": "0000000000000000000000000000000000000000000000000110000011000000111111111110000011100000111000000101101101000110010110110100011001000100011111100010000011100001011111111110011101100001110011111111111111111111111001110011110000000000000000000000000000000000",
    "penguin": "0000000000000000000000000000000000000000000000000000111110000000000110001100000000010010110000000011100011100000011110011110000000010000111110000011000001111100011100000011111000011000001100000000111111110000001111001110000000000000000000000000000000000000",
    "whale": "0000000000000000000000000000000000000000000000000011011000110010010010010011111100001000000111110011111000001110011111111000111011101111110111101111111111111110111111111111110011111101111111000111111000111000001111111111000000000000000000000000000000000000",
    "sheep": "000000000000000000000000000000000000000000000000000011011100000000110010001101100111100000001001111101000000010111011100000001101111000000000100111000000000010000101001010010000011111111111000001101101111000000000000000000000000000000000000"}

poop_bitmap = "0100100110010010010010011000001000011000001111000111111011111111"


def time_to_str(time):
    sec = time % 60
    time //= 60
    minutes = time % 60
    time //= 60
    hour = time % 24
    time //= 24
    answer = str(time) + " days, " + str(hour) + " hours, " + str(minutes) + " min, " + str(sec) + " sec"
    return answer


class Pet:
    def __init__(self, type, name, age,
                 food, health, joy, is_poop, time_to_poop, words, canv, root):
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
                self.picture.append(canv.create_rectangle(60 + x, 130 + y, 60 + x + 15, 130 + y + 15, fill="black"))
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
                        canv.create_rectangle(310 + x, 300 + y, 310 + x + 5, 300 + y + 5, fill='brown',
                                              outline='brown'))
                x += 5
                if x == 40:
                    x = 0
                    y += 5

        # add texts

        self.name_text = canv.create_text(180, 100, text=self.name, font=tkinter.font.Font(family='Helvetica', size=20))
        self.age_text = canv.create_text(375, 35, text="Your pet is " + time_to_str(self.age) + " old!",
                                         font=tkinter.font.Font(family='Helvetica', size=16))

        # add stats

        self.food_bar_border = canv.create_rectangle(430, 100, 480, 300, outline="red")
        self.health_bar_border = canv.create_rectangle(530, 100, 580, 300, outline="green")
        self.joy_bar_border = canv.create_rectangle(630, 100, 680, 300, outline="purple")

        self.food_bar = canv.create_rectangle(430, 100 + 200 - 2 * self.food, 480, 300, fill="red", outline="red")
        self.health_bar = canv.create_rectangle(530, 100 + 200 - 2 * self.health, 580, 300, fill="green",
                                                outline="green")
        self.joy_bar = canv.create_rectangle(630, 100 + 200 - 2 * self.joy, 680, 300, fill="purple", outline="purple")

        self.food_title = canv.create_text(455, 320, text="FOOD", fill="red", font=tkinter.font.Font(size=16))
        self.health_title = canv.create_text(555, 320, text="HEALTH", fill="green", font=tkinter.font.Font(size=16))
        self.joy_title = canv.create_text(655, 320, text="JOY", fill="purple", font=tkinter.font.Font(size=16))

        self.food_text = canv.create_text(455, 340, text=str(self.food) + "%", fill="red",
                                          font=tkinter.font.Font(size=16))
        self.health_text = canv.create_text(555, 340, text=str(self.health) + "%", fill="green",
                                            font=tkinter.font.Font(size=16))
        self.joy_text = canv.create_text(655, 340, text=str(self.joy) + "%", fill="purple",
                                         font=tkinter.font.Font(size=16))

        self.current_word = random.choice(self.words)
        self.phrase = canv.create_text(180, 450, text=self.current_word, font=tkinter.font.Font(size=18))

        self.pet_says = canv.create_text(180, 400, text="Your pet says:", font=tkinter.font.Font(size=18))

        self.feed_button = Button(root, text="Feed", background="red", font=16, command=lambda: self.update_food(5))
        self.feed_button.place(x=410, y=380, height=60, width=90)

        self.heal_button = Button(root, text="Heal", background="green", font=16, command=lambda: self.update_health(5))
        self.heal_button.place(x=510, y=380, height=60, width=90)

        self.play_button = Button(root, text="Play", background="purple", font=16, command=lambda: self.update_joy(5))
        self.play_button.place(x=610, y=380, height=60, width=90)

        self.clean_button = Button(root, text="Clean", background="yellow", font=16, command=lambda: self.clean())
        self.clean_button.place(x=410, y=450, height=60, width=90)

        self.talk_button = Button(root, text="Talk", background="light blue", font=16, command=lambda: self.talk())
        self.talk_button.place(x=510, y=450, height=60, width=90)

        self.teach_button = Button(root, text="Teach", background="pink", font=16, command=lambda: self.word_choice())
        self.teach_button.place(x=610, y=450, height=60, width=90)

    def save(self):
        datas = [self.type, self.name, self.age, self.food, self.health, self.joy, self.isPoop, self.timeToPoop,
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
                    self.food_bar_border, self.joy_bar_border, self.joy_title,
                    self.food_title, self.health_title)

        for pix in self.picture:
            self.canv.delete(pix)

        if self.isPoop:
            for pix in self.poop_picture:
                self.canv.delete(pix)

    def update_states(self):
        self.canv.delete(self.food_bar)
        self.canv.delete(self.health_bar)
        self.canv.delete(self.joy_bar)
        self.food_bar = self.canv.create_rectangle(430, 100 + 200 - 2 * self.food, 480, 300, fill="red", outline="red")
        self.health_bar = self.canv.create_rectangle(530, 100 + 200 - 2 * self.health, 580, 300, fill="green",
                                                outline="green")
        self.joy_bar = self.canv.create_rectangle(630, 100 + 200 - 2 * self.joy, 680, 300, fill="purple", outline="purple")

        self.canv.delete(self.food_text)
        self.canv.delete(self.health_text)
        self.canv.delete(self.joy_text)
        self.food_text = self.canv.create_text(455, 340, text=str(round(self.food, 2)) + "%", fill="red",
                                          font=tkinter.font.Font(size=16))
        self.health_text = self.canv.create_text(555, 340, text=str(round(self.health, 2)) + "%", fill="green",
                                            font=tkinter.font.Font(size=16))
        self.joy_text = self.canv.create_text(655, 340, text=str(round(self.joy, 2)) + "%", fill="purple",
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
                           command=lambda: self.learn_new_word(new_word.get(), enter_window))
        enter_but.place(x=120, y=60, width=60, height=40)
        new_word.pack()

    def talk(self):
        old_phrase = self.current_word
        while self.current_word == old_phrase:
            self.current_word = random.choice(self.words)
        self.canv.delete(self.phrase)
        self.phrase = self.canv.create_text(180, 450, text=self.current_word, font=tkinter.font.Font(size=18))

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
                    self.canv.create_rectangle(310 + x, 300 + y, 310 + x + 5, 300 + y + 5, fill='brown', outline='brown'))
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
        self.age_text = self.canv.create_text(375, 35, text="Your pet is " + time_to_str(self.age) + " old!",
                                         font=tkinter.font.Font(family='Helvetica', size=16))

        self.update_states()

        if self.timeToPoop == 0:
            self.poop()

        self.save()

        if self.hasRun:
            self.run_away()
