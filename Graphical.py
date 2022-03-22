from PySide6 import QtCore, QtWidgets, QtGui
from RandomWordGenerator import RandomWord
import time


class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()


        self.timer_flag = False
        self.checking_flag = False

        self.label = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.label.resize(360, 40)
        self.label.setStyleSheet("""
        font-size: 70px;
        padding: 5px;
        color: #D49B54;
        """)

        self.count = 5
        interval = 1200
        timer = QtCore.QTimer(self)
        timer.setInterval(1200)
        # Bardzo ważna formatka najważniejsza meeeega ważna
        QtCore.QObject.connect(timer, QtCore.SIGNAL("timeout()"), self.countdown)

        timer.start(1000)

        countown = QtWidgets.QHBoxLayout()
        countown.addWidget(self.label)

        self.descriprion = QtWidgets.QLabel("This program measures your typing speed,\n When you press"
                                       " the start button counting down will start"
                                       , alignment=QtCore.Qt.AlignCenter)


        self.inputer = QtWidgets.QLineEdit("Input the word displayed at the top after countdown"
                                           , alignment=QtCore.Qt.AlignCenter)
        self.inputer.setStyleSheet("""
        max-width: 450px;
        """)
        input = QtWidgets.QHBoxLayout()
        input.addWidget(self.inputer)



        self.button = QtWidgets.QPushButton("Start the game")
        self.button.setStyleSheet("""
        background-color: #D49B54;
        font-size: 18px;
        max-width: 120px;
        height: 50px;
        """)


        self.measure_button = QtWidgets.QPushButton("Check my speeed")
        self.measure_button.setStyleSheet("""
        background-color: #C74B50;
        font-size: 18px;
        max-width: 180px;
        height: 50px;
        """)

        buttons = QtWidgets.QHBoxLayout()
        buttons.addWidget((self.button))
        buttons.addWidget(self.measure_button)

        self.measure_button.clicked.connect(self.checking)

        self.button.clicked.connect(self.word_draw)
        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.label)
        self.layout.addWidget(self.descriprion)

        self.layout.addLayout(countown)
        self.layout.addLayout(input)
        self.layout.addLayout(buttons)




    @QtCore.Slot()
    def countdown(self):
        # global count
        if self.count == 0:
            self.display_word()
        if self.timer_flag and self.count > 0:
            self.count = self.count - 1
            self.label.setText(f'{self.count}')



    @QtCore.Slot()
    def word_draw(self):
        self.checking_flag = False
        self.count = 6
        self.timer_flag = True
        self.inputer.setText("")
        rw = RandomWord(max_word_size=10)
        self.generated_word = rw.generate()
        self.start_time = time.time()
        # print(self.generated_word)



    @QtCore.Slot()
    def display_word(self):

        self.checking_flag = True
        self.label.setText(self.generated_word)



    @QtCore.Slot()
    def checking(self):
        print(self.inputer.text())
        if self.inputer.text() == self.generated_word:
            self.stop_time = time.time()
            typing_time = self.stop_time - self.start_time
            self.descriprion.setText(f"Your typing time was {round(typing_time, 4)} s")
        else:
            self.descriprion.setText("Sory sentence you typed was Invalid Try again")
        print('enter')


