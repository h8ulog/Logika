from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app=QApplication([])
win=QWidget()
win.setWindowTitle('Визначник переможця')
win.resize(400,200)
win.move(500,200)
text=QLabel(win)
text.setText("Натисніть щоб дізнатись переможця")
text.move(110,30)

text2=QLabel(win)
text2.setText("?")
text2.move(197,70)

button=QPushButton(win)
button.setText("Згенерувати")
button.move(160,150)

def show_win():
    number=randint(1,100)
    text2.setText(str(number))
    text.setText("Переможець")
    text.move(170,30)
button.clicked.connect(show_win)
win.show()
app.exec()
