import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from StudentsRepository import Students


class StudentDetailWindow(QWidget):

    def __init__(self, id):
        super().__init__()
        self.db = Students()
        self.info = self.db.getById(id)

        self.setGeometry(300, 400, 300 , 300)
        self.verticalLay = QVBoxLayout(self)
        self.id = QLabel(f"ID: {self.info.id}", self)
        self.firstName = QLabel(f"FIRST NAME: {self.info.firstName}", self)
        self.lastName = QLabel(f"LAST NAME: {self.info.lastName}", self)
        self.age = QLabel(f"AGE: {self.info.age}", self)
        self.course = QLabel(f"COURSE: {self.info.course}", self)

        self.deleteBtn = QPushButton("Delete",self)
        self.deleteBtn.clicked.connect(self.deleteStudent)
        
        self.verticalLay.addWidget(self.id)    
        self.verticalLay.addWidget(self.firstName)
        self.verticalLay.addWidget(self.lastName)
        self.verticalLay.addWidget(self.age)
        self.verticalLay.addWidget(self.course)

        self.setLayout(self.verticalLay)

    def deleteStudent(self):
        res = self.db.deleteById(self.info.id)
        if( not res ):
            print("hatolik")


class Window(QWidget):
    page = 1
    page_size = 3
    def __init__(self):
        super().__init__()
        self.studentRepo = Students()



        self.vLayout = QVBoxLayout(self)
        self.qLstW = QListWidget(self)

        self.vLayout.addWidget(self.qLstW)

        self.btnPrev = QPushButton("Prev",self )
        self.btnNext = QPushButton("Next",self )

        self.hLayout = QHBoxLayout(self)

        self.hLayout.addWidget(self.btnPrev)
        self.hLayout.addWidget(self.btnNext)

        self.vLayout.addLayout(self.hLayout)


        self.setLayout(self.vLayout)

        self.btnNext.clicked.connect(self.getNextStudents)
        self.btnPrev.clicked.connect(self.getPrevStudents)
        self.qLstW.itemClicked.connect(self.showStudentDetail)

        self.mainQhLay = QHBoxLayout(self)
        self.searchLineEdit = QLineEdit(self)
        self.courseCombo = QComboBox(self)
        self.mainQhLay.addWidget(self.searchLineEdit)
        self.mainQhLay.addWidget(self.courseCombo)
        
        self.vLayout.addLayout(self.mainQhLay)

        self.setUsersToListWidget()
        self.courseCombo.addItems(["all","1", "2", "3", "4"])

        self.searchLineEdit.textChanged.connect(self.setUsersToListWidget)
        self.courseCombo.activated.connect(self.setUsersToListWidget)



    def setUsersToListWidget(self):
        self.qLstW.clear()
        search = ""
        course = 0
        if( self.searchLineEdit.text() ):
            search = self.searchLineEdit.text()
        
        if(self.courseCombo.currentText() and self.courseCombo.currentText() != "all" ):
            course = int(self.courseCombo.currentText())

        for item in self.studentRepo.getStudentsList(page=self.page, size=self.page_size, search = search, course = course):
            newItem = QListWidgetItem(item.firstName + " " + item.lastName)
            newItem.studentId = item.id
            self.qLstW.addItem(newItem)

    def getNextStudents(self):
        self.btnPrev.setEnabled(True)
        self.page += 1
        self.setUsersToListWidget()

    def getPrevStudents(self):
        if(self.page == 1):
            self.btnPrev.setEnabled(False)
            return
        self.page -= 1
        self.setUsersToListWidget()

    def showStudentDetail(self):
        # print(self.qLstW.currentItem().studentId)
        self.detailWindow = StudentDetailWindow(self.qLstW.currentItem().studentId )
        self.detailWindow.show()




app = QApplication([])
wn = Window()
wn.show()
app.exec_()