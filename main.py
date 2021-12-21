from PyQt5.QtCore import right
import PyQt5.QtWidgets as qtw
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtWidgets
import os
from script import Convertor


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.left_array = None
        self.right_array = None

        self.unique_array = []

        loadUi("ui/main.ui", self)

        self.convertor = Convertor()

        self.browseleft.clicked.connect(lambda: self.browsefiles(
            title='Select Left csv file', lineedit=self.filepathleft))
        self.browseright.clicked.connect(lambda: self.browsefiles(
            title='Select Right csv file', lineedit=self.filepathright))

        self.unqiuebutton.clicked.connect(lambda: self.generate_unique_csv())

        # self.filterbutton.clicked.connect(lambda : self.filter_two_csv())

    def generate_unique_csv(self):

        print(self.left_array, self.right_array, self.unique_array)

        if self.right_array is not None and self.left_array is not None:

            self.unique_array = self.convertor.filter_array(left_file_array=self.left_array, right_file_array=self.right_array)

            try:
                msg = self.convertor.array_to_csv(
                    np_array=self.unique_array, filename="unique_file_app.csv")
                qtw.QMessageBox.about(self, "Message", msg)
                
                self.left_array = None
                self.right_array = None
                self.unique_array = []

                self.filepathleft.setText('')
                self.filepathright.setText('')

            except Exception as e:
                msg = str(e)

        else:
            qtw.QMessageBox.about(
                self, "Message", "Please Make sure both CSV's are loaded!!")

    def browsefiles(self, title, lineedit, defaultpath='C:\\'):

        file = qtw.QFileDialog.getOpenFileName(
            self, title, defaultpath, 'CSV Files (*.csv, *.csv)')
        lineedit.setText(file[0])

        # print(lineedit.text())

        if "left" in title.lower():

            self.left_array = self.convertor.read_csv_file(
                path=lineedit.text())
        elif "right" in title.lower():
            self.right_array = self.convertor.read_csv_file(
                path=lineedit.text())

        # print(self.left_array, self.right_array)

        # if self.left_array is None or self.right_array is None:
        #     self.uniquebutton.setEnabled(True)
        # else:
        #     self.uniquebutton.setEnabled(False)


app = qtw.QApplication(sys.argv)


mainwindow = MainWindow()



widget = qtw.QStackedWidget()

widget.setWindowTitle("Leads Filter TMC")

widget.addWidget(mainwindow)

widget.setFixedWidth(700)
widget.setFixedHeight(150)

widget.show()

sys.exit(app.exec_())
