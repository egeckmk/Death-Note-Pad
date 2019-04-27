from PyQt5 import QtWidgets
from views.main_view import MainView
from models.model import Model
from controllers.main_ctrl import MainController
import sys


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App,self).__init__(sys_argv)
    
        self._model =Model()
        self._main_controller = MainController(self._model)
        self._main_view = MainView(self._model,self._main_controller)
        self._main_view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())




