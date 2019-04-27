from PyQt5 import QtWidgets
from views.main_view_ui import Ui_MainWindow


class MainView(QtWidgets.QMainWindow):
    def __init__(self,model,conroller):
        super().__init__()

        self._model = model
        self._controller = conroller

        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
