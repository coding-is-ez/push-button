from guizero import App, Text, Box, info, PushButton, Picture
from random import choice
import PIL

window = App(title = "Find the spy", layout = "grid")

gened_box = Box(window, layout = "grid", grid = [0, 0], border = 5)

persons = []

very_sussy = ["very_sus.png", "very_sus_2.png"]

def correct(a: int, b: int, spy_button: PushButton):
        global very_sussy
        info(title = "Congratulations!", text = "You guessed correctly!")
        spy_button.destroy()
        pic = Picture(gened_box, image = choice(very_sussy), grid = [a, b])
        pic.resize(width = 175, height = 175)
        
def wrong():
    info(title = "FAHHH!!!!", text = "WRONG! GUESS AGAIN!")


def guess(a: int, b: int, spy_button: PushButton):
    global spy
    if [a, b] == spy:
        correct(a, b, spy_button)
    else:
        wrong()
    
for i in range(3):
    for j in range(3):
        btn = PushButton(gened_box, text = "?", grid = [i, j], width = 20, height = 10)
        btn.update_command(guess, args = [i, j, btn])
        persons.append([i, j])

spy = choice(persons)
print(spy)

# Run app
window.display()