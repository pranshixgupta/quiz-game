import pgzrun 
WIDTH = 700
HEIGHT = 600

titlebox = Rect(0,0,700,80)
questionbox = Rect(0,110,550,100)
timerbox = Rect(560,110, 150, 100)
answerbox1 = Rect(0,230,270,150 )
answerbox2 = Rect(280,230, 270, 150)
answerbox3 = Rect(0,390, 270, 150)
answerbox4 = Rect(280,390,270,150)
skip = Rect(560, 230, 140, 150)
reset = Rect(560, 390, 140, 150)

timer = 10 

def draw():
    screen.fill("black")
    screen.draw.filled_rect(titlebox, "pink")
    screen.draw.textbox("welcome to this quiz", titlebox, color = "black")
    screen.draw.filled_rect(questionbox, "green")
    screen.draw.filled_rect(timerbox, "dark green")
    screen.draw.textbox(str(timer), timerbox, color = "white")

    screen.draw.filled_rect(answerbox1, "purple")
    screen.draw.filled_rect(answerbox2, "purple")
    screen.draw.filled_rect(skip, "orange")
    screen.draw.textbox("skip", skip, color = "white")
    screen.draw.filled_rect(answerbox3, "purple")
    screen.draw.filled_rect(answerbox4, "purple")
    screen.draw.filled_rect(reset, "blue")
    screen.draw.textbox("reset", reset, color = "white")


questions = []
file = open("questions.txt", "r")
for question in file:
    questions.append(question)

question = questions.pop(0).split('|')


print(question)
file.close()

pgzrun.go()