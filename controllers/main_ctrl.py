from PyQt5 import QtCore
import os


class MainController(QtCore.QObject):
    def __init__(self,model):
        super().__init__()

        self._model = model

        self._main_path = os.path.expanduser("~/Death Note")
        self.file_path("Notes")
        
    def file_path(self,directory = ''):
        
        note_path = os.path.join(self._main_path, directory)
       
        if not os.path.exists(note_path):
            os.makedirs(note_path)
        return note_path

