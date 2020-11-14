#https://www.youtube.com/watch?v=Vde5SH8e1OQ&t=117s


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setGeometry(200,200,300,300)
    self.setWindowTitle("Tut 01")
    self.initUI()

  def initUI(self):

    self.label = QtWidgets.QLabel(self)
    self.label.setText("My Label")
    self.label.move(50,50)
  
    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("Push me")
    self.b1.clicked.connect(self.clicked)

  def clicked(self):
    self.label.setText("You clicked my button.")
    self.update()

  def update(self):
    self.label.adjustSize()



def window():
  app = QApplication(sys.argv)
  win = MyWindow()

  win.show()
  sys.exit(app.exec_())


window()

