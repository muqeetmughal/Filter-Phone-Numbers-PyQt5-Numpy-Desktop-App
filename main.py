from PyQt5.QtCore import right
import PyQt5.QtWidgets as qtw
from PyQt5.uic import loadUi
import sys
import os
from script import Convertor
from PyQt5 import QtGui
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.left_array = None
        
        self.right_array = None

        self.unique_array = []

        loadUi(os.path.join(BASE_DIR,"ui/main.ui"), self)

        self.convertor = Convertor()

        self.filepathleft.setEnabled(False)

        self.filepathright.setEnabled(False)

        self.browseleft.clicked.connect(lambda: self.browsefiles(
            title='Select Left csv file', lineedit=self.filepathleft))
        self.browseright.clicked.connect(lambda: self.browsefiles(
            title='Select Right csv file', lineedit=self.filepathright))

        self.sortedbutton.clicked.connect(
            lambda: self.generate_unique_csv(method="sorted"))

        self.unsortedbutton.clicked.connect(
            lambda: self.generate_unique_csv(method="unsorted"))

        self.enable_header.stateChanged.connect(self.is_header_enabled)

        # self.is_header_enabled()

    def is_header_enabled(self):

        print(self.enable_header.isChecked())

        if self.enable_header.isChecked():
            self.header = True
        else:
            self.header = False

    def generate_unique_csv(self, method):

        self.is_header_enabled()

        if self.right_array is not None and self.left_array is not None:

            self.unique_array = self.convertor.filter_array(
                left_file_array=self.left_array, right_file_array=self.right_array)

            output_path = str(qtw.QFileDialog.getExistingDirectory(
                self, "Select Directory"))
            try:
                import time

                print(output_path)
                msg = self.convertor.array_to_csv(method=method, header=self.header, np_array=self.unique_array, filename=os.path.join(
                    output_path, f"unique_scrubbed_{time.strftime('%Y%m%d-%H%M%S')}.csv"))
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

    def browsefiles(self, title, lineedit, defaultpath=""):

        file = qtw.QFileDialog.getOpenFileName(
            self, title, defaultpath, 'CSV Files (*.csv *.txt)')
        lineedit.setText(file[0])

        if "left" in title.lower():

            self.left_array = self.convertor.read_csv_file(
                path=lineedit.text())
        elif "right" in title.lower():
            self.right_array = self.convertor.read_csv_file(
                path=lineedit.text())


if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    mainwindow = MainWindow()

    styleSheet = """
        
        
        QMainWindow {
            background-color : #0c4c7c;
            color : white;
        }

        QPushButton {
            border:2px solid black; 
            background-color : #82a4bc;
            width : 100%;
            height : auto;
        }
        QLineEdit {
            height: 100%;
            width : 100%;
            color : black;
            background-color : white;
            border:2px solid black;
        }


        QLabel{
            color : white;
        }
        QCheckBox{
            color : white;
        }
        QMessageBox{
            background-color : #0c4c7c;
            color : white;
        }
        """

    app.setStyleSheet(styleSheet)

    widget = qtw.QStackedWidget()

    widget.setWindowTitle("Best Data Deals Scrubbing Tool")
    widget.setWindowIcon(QtGui.QIcon('logo.png'))

    widget.addWidget(mainwindow)

    # widget.setFixedWidth(1920)
    # widget.setFixedHeight(1080)
    # widget.showMaximized()
    widget.show()

    sys.exit(app.exec_())
