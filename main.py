import sys
from PySide6 import QtCore, QtWidgets, QtGui
from Graphical import MyWidget


from PySide6.QtWidgets import QApplication, QPushButton

# print(morse_alphabet)

def on_press(key):
    print(key)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])




    widget = MyWidget()
    widget.resize(600, 300)
    widget.setStyleSheet("""
        border-color: #557B83;
        background-color: #557B83;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;


    """)

    widget.show()



    # with Listener(
    #         on_press=on_press) as listener:
    #     listener.join()


    sys.exit(app.exec())
