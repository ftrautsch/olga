from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QWidget, QLabel, QPushButton, QFileDialog


class ConfigurationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ConfigurationWindow, self).__init__(parent)
        self.parent = parent

        self.baseline = QLineEdit(str(self.parent.configuration.baseline_time))
        self.cell_types = QLineEdit(str(self.parent.configuration.get_cell_types()))
        self.treatment = QLineEdit(str(self.parent.configuration.get_treatments()))
        self.file_dialog = QPushButton("File...")#
        self.output_dialog = QPushButton("File...")

        self.initUi()

    def initUi(self):
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.file_dialog.clicked.connect(self.openFileNameDialog)
        self.output_dialog.clicked.connect(self.output_file_dialog)

        grid.addWidget(QLabel("Baseline Time"), 0, 0)
        grid.addWidget(QLabel("Cell Types"), 1, 0)
        grid.addWidget(QLabel("Treatments"), 2, 0)
        grid.addWidget(QLabel("Input File"), 3, 0)
        grid.addWidget(QLabel("Output File"), 4, 0)
        grid.addWidget(self.baseline, 0, 1)
        grid.addWidget(self.cell_types, 1, 1)
        grid.addWidget(self.treatment, 2, 1)
        grid.addWidget(self.file_dialog, 3, 1)
        grid.addWidget(self.output_dialog, 4, 1)
        widget.show()
        self.show()

    def closeEvent(self, event):
        self.parent.configuration.baseline_time = int(self.baseline.text())
        self.parent.configuration.set_cell_types(self.cell_types.text())
        self.parent.configuration.set_treatments(self.treatment.text())

    @pyqtSlot()
    def output_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Store Output", "",
                                                  "All Files (*);;CSV Files (*.csv)", options=options)
        if fileName:
            self.output_dialog.setText(fileName)
            self.parent.configuration.output = fileName

    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Txt Files (*.txt)", options=options)
        if fileName:
            self.file_dialog.setText(fileName)
            self.parent.configuration.input = fileName
