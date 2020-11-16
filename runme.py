import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets 




class Window(QtWidgets.QMainWindow):
    """Main window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        loadUi('.\\ui\\test.ui',self)

        #Get UI Widgets
        self.button01 = self.findChild(QtWidgets.QPushButton, 'button01')
        self.comboBox = self.findChild(QtWidgets.QComboBox, 'comboBox')

        self.loadCombo()
        self.button01.clicked.connect(buttonPressed)
    
    def loadCombo(self):
        print("Load Combo")
    

def buttonPressed():
        print ("Pressed")

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    # Create and show the application's main window
    win = Window()
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())