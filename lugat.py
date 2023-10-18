from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from StudentsRepository import Students
from Application import Application


class Dictionary(QWidget):

    currentLang = "English"

    def __init__(self):
        super().__init__()
        self.app = Application()
        self.dbConnection = self.app.getConnection()
        self.dbCursor = self.dbConnection.cursor()
        self.frontSettings()

    def frontSettings(self):
        self.setFixedSize(500, 400)
        self.line1 = QLineEdit(self)
        self.changeLang = QComboBox( self)
        self.changeLang.addItems(["English", "Uzbek"])
        self.findLabel = QLabel("Some text",self)
        self.listWords = QListWidget(self)

        self.line1.setStyleSheet("font-size: 20px")
        self.findLabel.setStyleSheet("font-size: 20px")
        self.changeLang.setStyleSheet("font-size: 20px")
        self.listWords.setStyleSheet("font-size: 20px")



        self.hLay = QGridLayout(self)
        self.hLay.addWidget(self.line1, 0, 0)
        self.hLay.addWidget(self.changeLang, 0, 1)
        self.hLay.addWidget(self.findLabel, 0, 2)
        self.hLay.addWidget(self.listWords, 1, 0,  1, 3)
        

        self.setLayout(self.hLay)

        self.line1.textChanged.connect(self.setTextToWidget)
        self.listWords.itemClicked.connect(self.setTranslated)
        self.changeLang.activated.connect(self.changeLanguage)

    def changeLanguage(self):
        self.currentLang = self.changeLang.currentText()
        self.setTextToWidget()

    def setTranslated(self):
        self.findLabel.setText(self.listWords.currentItem().translated)



    def setTextToWidget(self):
        if( not self.line1.text() ):
            self.listWords.clear()
            return
        
        allWords = None
        if( self.currentLang == "English" ):
            allWords = self.getEnglishWords()
        else:
            allWords = self.getUzbekhWords()

        self.listWords.clear()
        

        for item in allWords:
            newItem = QListWidgetItem(item[0])
            newItem.translated = item[1]
            self.listWords.addItem(newItem)


    def getEnglishWords(self):

        query = """select word_1, word_2 from word where word_1 like concat('%', %s, '%') order by word_1"""

        self.dbCursor.execute(query, (self.line1.text(), ))

        return self.dbCursor.fetchall()

    def getUzbekhWords(self):

        query = """select word_2, word_1 from word where word_2 like concat('%', %s, '%') order by word_2"""

        self.dbCursor.execute(query, (self.line1.text(), ))

        return self.dbCursor.fetchall()



app = QApplication([])
wn = Dictionary()
wn.show()
app.exec_()