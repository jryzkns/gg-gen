from PyQt5.QtWidgets import QApplication
from ggapp import GGApp
import sys

if __name__ == '__main__':
    m = QApplication(sys.argv)
    app = GGApp()
    app.show()
    sys.exit(m.exec_())