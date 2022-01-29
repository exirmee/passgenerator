
import string
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import passGenGui

# Create Init function and call gui from passGenGui.py
class passGenApp(QtWidgets.QMainWindow, passGenGui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(passGenApp, self).__init__(parent)
        self.setupUi(self)
        passGenGui.Ui_MainWindow.reloadPass(self)
def main():
    app = QApplication(sys.argv)
    form = passGenApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()


# This function creates a password combination of uppercase and lowercase letters and numbers and 
# special characters of any length #Inputs of this function in order: Password length. Lowercase letters. 
# Uppercase letters .numbers. Special characters
def passGen(passlenght,lowChar,capChar,numChar,sigChar):
    # Define a variable to put the value of the password in it
    password=''    #
    passChars=''
    # Using the IF command and the string module we check what characters 
    #(uppercase and lowercase numbers and characters) are needed for the password and put them in the variable    
    if lowChar:passChars=string.ascii_lowercase
    if capChar:passChars=passChars+string.ascii_uppercase
    if numChar:passChars=passChars+string.digits
    if sigChar:passChars=passChars+string.punctuation
    if lowChar==False and capChar==False and numChar==False and sigChar==False :passChars='*'
    for i in range(passlenght):
        # Each time the loop is called, a character is randomly selected from a 
        # variable of letters, numbers, and characters.
        ch=random.choice(passChars)
        # The selected character is added to the password variable
        password+=ch
    return password



