import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, qApp)

from analysiswidget import AnalysisWidget
from configuration import Configuration
from configuration_window import ConfigurationWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.analysis_widget = AnalysisWidget(self)
        self.setCentralWidget(self.analysis_widget)
        self.configuration_window = None
        self.configuration = Configuration()

        self.initUI()

    def initUI(self):
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        setConfigurationAct = QAction('&Configuration', self)
        setConfigurationAct.setShortcut('Ctrl+C')
        setConfigurationAct.setStatusTip('Set Configuration')
        setConfigurationAct.triggered.connect(self.showConfiguration)

        self.statusBar()

        menubar = self.menuBar()
        menu = menubar.addMenu('&Configuration')
        menu.addAction(setConfigurationAct)
        menu.addAction(exitAct)

    def showConfiguration(self):
        if not self.configuration_window:
            self.configuration_window = ConfigurationWindow(self)
        self.configuration_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())