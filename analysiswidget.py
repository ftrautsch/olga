import sys

from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QTextEdit

from analyze import PlateAnalysis
from configuration import Measurement


class EmittingStream(QObject):

    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class AnalysisWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.initialize_line_edits()
        self.text_edit = QTextEdit()

        sys.stdout = EmittingStream(textWritten=self.normal_output_written)


        self.initUI()

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normal_output_written(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        widgets = [
            None, QLabel('1'), QLabel('2'), QLabel('3'), QLabel('4'), QLabel('5'), QLabel('6'), QLabel('7'), QLabel('8'), QLabel('9'), QLabel('10'), QLabel('11'), QLabel('12'),
            QLabel('A'), self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9, self.a10, self.a11, self.a12,
            QLabel('B'), self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10, self.b11, self.b12,
            QLabel('C'), self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10, self.c11, self.c12,
            QLabel('D'), self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11, self.d12,
            QLabel('E'), self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9, self.e10, self.e11, self.e12,
            QLabel('F'), self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12,
            QLabel('G'), self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9, self.g10, self.g11, self.g12,
            QLabel('H'), self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8, self.h9, self.h10, self.h11, self.h12,
            None, self.cell_type1, self.cell_type2, self.cell_type3, self.cell_type4, self.cell_type5, self.cell_type6, self.cell_type7, self.cell_type8, self.cell_type9, self.cell_type10, self.cell_type11, self.cell_type12,
        ]

        positions = [(i, j) for i in range(10) for j in range(13)]

        for position, widget in zip(positions, widgets):

            if widget is None:
                continue
            else:
                grid.addWidget(widget, *position)

        grid.addWidget(QLabel("Output"), 10, 1)
        grid.addWidget(self.text_edit, 11, 1)


        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.close_window)
        grid.addWidget(quit_button, 12, 12)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_analysis)
        grid.addWidget(start_button, 12, 1)

        self.move(300, 150)
        self.setWindowTitle('Irinas Olga Tool')
        self.show()

    @pyqtSlot()
    def start_analysis(self):
        # Create all measurements

        measurements = [
            [Measurement("A1", self.cell_type1.text(), self.a1.text()), Measurement("A2", self.cell_type2.text(), self.a2.text()),
             Measurement("A3", self.cell_type3.text(), self.a3.text()), Measurement("A4", self.cell_type4.text(), self.a4.text()),
             Measurement("A5", self.cell_type5.text(), self.a5.text()),  Measurement("A6", self.cell_type6.text(), self.a6.text()),
             Measurement("A7",self.cell_type7.text(), self.a7.text()), Measurement("A8", self.cell_type8.text(),self.a8.text()),
             Measurement("A9", self.cell_type9.text(), self.a9.text()), Measurement("A10", self.cell_type10.text(), self.a10.text()),
             Measurement("A11", self.cell_type11.text(), self.a11.text()),  Measurement("A12", self.cell_type12.text(), self.a12.text())],
            [Measurement("B1", self.cell_type1.text(), self.b1.text()), Measurement("B2", self.cell_type2.text(), self.b2.text()),
             Measurement("B3", self.cell_type3.text(), self.b3.text()), Measurement("B4", self.cell_type4.text(), self.b4.text()),
             Measurement("B5", self.cell_type5.text(), self.b5.text()),  Measurement("B6", self.cell_type6.text(), self.b6.text()),
             Measurement("B7",self.cell_type7.text(), self.b7.text()), Measurement("B8", self.cell_type8.text(),self.b8.text()),
             Measurement("B9", self.cell_type9.text(), self.b9.text()), Measurement("B10", self.cell_type10.text(), self.b10.text()),
             Measurement("B11", self.cell_type11.text(), self.b11.text()),  Measurement("B12", self.cell_type12.text(), self.b12.text())],
            [Measurement("C1", self.cell_type1.text(), self.c1.text()), Measurement("C2", self.cell_type2.text(), self.c2.text()),
             Measurement("C3", self.cell_type3.text(), self.c3.text()), Measurement("C4", self.cell_type4.text(), self.c4.text()),
             Measurement("C5", self.cell_type5.text(), self.c5.text()),  Measurement("C6", self.cell_type6.text(), self.c6.text()),
             Measurement("C7",self.cell_type7.text(), self.c7.text()), Measurement("C8", self.cell_type8.text(),self.c8.text()),
             Measurement("C9", self.cell_type9.text(), self.c9.text()), Measurement("C10", self.cell_type10.text(), self.c10.text()),
             Measurement("C11", self.cell_type11.text(), self.c11.text()),  Measurement("C12", self.cell_type12.text(), self.c12.text())],
            [Measurement("D1", self.cell_type1.text(), self.d1.text()), Measurement("D2", self.cell_type2.text(), self.d2.text()),
             Measurement("D3", self.cell_type3.text(), self.d3.text()), Measurement("D4", self.cell_type4.text(), self.d4.text()),
             Measurement("D5", self.cell_type5.text(), self.d5.text()),  Measurement("D6", self.cell_type6.text(), self.d6.text()),
             Measurement("D7",self.cell_type7.text(), self.d7.text()), Measurement("D8", self.cell_type8.text(),self.d8.text()),
             Measurement("D9", self.cell_type9.text(), self.d9.text()), Measurement("D10", self.cell_type10.text(), self.d10.text()),
             Measurement("D11", self.cell_type11.text(), self.d11.text()),  Measurement("D12", self.cell_type12.text(), self.d12.text())],
            [Measurement("E1", self.cell_type1.text(), self.e1.text()), Measurement("E2", self.cell_type2.text(), self.e2.text()),
             Measurement("E3", self.cell_type3.text(), self.e3.text()), Measurement("E4", self.cell_type4.text(), self.e4.text()),
             Measurement("E5", self.cell_type5.text(), self.e5.text()),  Measurement("E6", self.cell_type6.text(), self.e6.text()),
             Measurement("E7",self.cell_type7.text(), self.e7.text()), Measurement("E8", self.cell_type8.text(),self.e8.text()),
             Measurement("E9", self.cell_type9.text(), self.e9.text()), Measurement("E10", self.cell_type10.text(), self.e10.text()),
             Measurement("E11", self.cell_type11.text(), self.e11.text()),  Measurement("E12", self.cell_type12.text(), self.e12.text())],
            [Measurement("F1", self.cell_type1.text(), self.f1.text()), Measurement("F2", self.cell_type2.text(), self.f2.text()),
             Measurement("F3", self.cell_type3.text(), self.f3.text()), Measurement("F4", self.cell_type4.text(), self.f4.text()),
             Measurement("F5", self.cell_type5.text(), self.f5.text()),  Measurement("F6", self.cell_type6.text(), self.f6.text()),
             Measurement("F7",self.cell_type7.text(), self.f7.text()), Measurement("F8", self.cell_type8.text(),self.f8.text()),
             Measurement("F9", self.cell_type9.text(), self.f9.text()), Measurement("F10", self.cell_type10.text(), self.f10.text()),
             Measurement("F11", self.cell_type11.text(), self.f11.text()),  Measurement("F12", self.cell_type12.text(), self.f12.text())],
            [Measurement("G1", self.cell_type1.text(), self.g1.text()), Measurement("G2", self.cell_type2.text(), self.g2.text()),
             Measurement("G3", self.cell_type3.text(), self.g3.text()), Measurement("G4", self.cell_type4.text(), self.g4.text()),
             Measurement("G5", self.cell_type5.text(), self.g5.text()),  Measurement("G6", self.cell_type6.text(), self.g6.text()),
             Measurement("G7",self.cell_type7.text(), self.g7.text()), Measurement("G8", self.cell_type8.text(),self.g8.text()),
             Measurement("G9", self.cell_type9.text(), self.g9.text()), Measurement("G10", self.cell_type10.text(), self.g10.text()),
             Measurement("G11", self.cell_type11.text(), self.g11.text()),  Measurement("G12", self.cell_type12.text(), self.g12.text())],
            [Measurement("H1", self.cell_type1.text(), self.h1.text()), Measurement("H2", self.cell_type2.text(), self.h2.text()),
             Measurement("H3", self.cell_type3.text(), self.h3.text()), Measurement("H4", self.cell_type4.text(), self.h4.text()),
             Measurement("H5", self.cell_type5.text(), self.h5.text()),  Measurement("H6", self.cell_type6.text(), self.h6.text()),
             Measurement("H7",self.cell_type7.text(), self.h7.text()), Measurement("H8", self.cell_type8.text(),self.h8.text()),
             Measurement("H9", self.cell_type9.text(), self.h9.text()), Measurement("H10", self.cell_type10.text(), self.h10.text()),
             Measurement("H11", self.cell_type11.text(), self.h11.text()),  Measurement("H12", self.cell_type12.text(), self.h12.text())],
        ]

        if self.parent.configuration.isValid():
            plate_analysis = PlateAnalysis(self.parent.configuration.input, self.parent.configuration.output, measurements)
            plate_analysis.create_output(self.parent.configuration.baseline_time, self.parent.configuration.cell_types,
                                         self.parent.configuration.treatments)
        else:
            message = QMessageBox.question(self, 'Configuration not Valid',
                                           'Configuration %s is not valid' % self.parent.configuration, QMessageBox.Ok,
                                           QMessageBox.Ok)

    @pyqtSlot()
    def close_window(self):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.parent.close()

    def initialize_line_edits(self):
        self.a1 = QLineEdit()
        self.a2 = QLineEdit()
        self.a3 = QLineEdit()
        self.a4 = QLineEdit()
        self.a5 = QLineEdit()
        self.a6 = QLineEdit()
        self.a7 = QLineEdit()
        self.a8 = QLineEdit()
        self.a9 = QLineEdit()
        self.a10 = QLineEdit()
        self.a11 = QLineEdit()
        self.a12 = QLineEdit()

        self.b1 = QLineEdit()
        self.b2 = QLineEdit()
        self.b3 = QLineEdit()
        self.b4 = QLineEdit()
        self.b5 = QLineEdit()
        self.b6 = QLineEdit()
        self.b7 = QLineEdit()
        self.b8 = QLineEdit()
        self.b9 = QLineEdit()
        self.b10 = QLineEdit()
        self.b11 = QLineEdit()
        self.b12 = QLineEdit()

        self.c1 = QLineEdit()
        self.c2 = QLineEdit()
        self.c3 = QLineEdit()
        self.c4 = QLineEdit()
        self.c5 = QLineEdit()
        self.c6 = QLineEdit()
        self.c7 = QLineEdit()
        self.c8 = QLineEdit()
        self.c9 = QLineEdit()
        self.c10 = QLineEdit()
        self.c11 = QLineEdit()
        self.c12 = QLineEdit()

        self.d1 = QLineEdit()
        self.d2 = QLineEdit()
        self.d3 = QLineEdit()
        self.d4 = QLineEdit()
        self.d5 = QLineEdit()
        self.d6 = QLineEdit()
        self.d7 = QLineEdit()
        self.d8 = QLineEdit()
        self.d9 = QLineEdit()
        self.d10 = QLineEdit()
        self.d11 = QLineEdit()
        self.d12 = QLineEdit()

        self.e1 = QLineEdit()
        self.e2 = QLineEdit()
        self.e3 = QLineEdit()
        self.e4 = QLineEdit()
        self.e5 = QLineEdit()
        self.e6 = QLineEdit()
        self.e7 = QLineEdit()
        self.e8 = QLineEdit()
        self.e9 = QLineEdit()
        self.e10 = QLineEdit()
        self.e11 = QLineEdit()
        self.e12 = QLineEdit()

        self.f1 = QLineEdit()
        self.f2 = QLineEdit()
        self.f3 = QLineEdit()
        self.f4 = QLineEdit()
        self.f5 = QLineEdit()
        self.f6 = QLineEdit()
        self.f7 = QLineEdit()
        self.f8 = QLineEdit()
        self.f9 = QLineEdit()
        self.f10 = QLineEdit()
        self.f11 = QLineEdit()
        self.f12 = QLineEdit()

        self.g1 = QLineEdit()
        self.g2 = QLineEdit()
        self.g3 = QLineEdit()
        self.g4 = QLineEdit()
        self.g5 = QLineEdit()
        self.g6 = QLineEdit()
        self.g7 = QLineEdit()
        self.g8 = QLineEdit()
        self.g9 = QLineEdit()
        self.g10 = QLineEdit()
        self.g11 = QLineEdit()
        self.g12 = QLineEdit()

        self.h1 = QLineEdit()
        self.h2 = QLineEdit()
        self.h3 = QLineEdit()
        self.h4 = QLineEdit()
        self.h5 = QLineEdit()
        self.h6 = QLineEdit()
        self.h7 = QLineEdit()
        self.h8 = QLineEdit()
        self.h9 = QLineEdit()
        self.h10 = QLineEdit()
        self.h11 = QLineEdit()
        self.h12 = QLineEdit()

        self.cell_type1 = QLineEdit()
        self.cell_type2 = QLineEdit()
        self.cell_type3 = QLineEdit()
        self.cell_type4 = QLineEdit()
        self.cell_type5 = QLineEdit()
        self.cell_type6 = QLineEdit()
        self.cell_type7 = QLineEdit()
        self.cell_type8 = QLineEdit()
        self.cell_type9 = QLineEdit()
        self.cell_type10 = QLineEdit()
        self.cell_type11 = QLineEdit()
        self.cell_type12 = QLineEdit()