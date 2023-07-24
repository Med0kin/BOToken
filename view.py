from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("BOTokens")
        self._setup_ui()
        self.show()

    def _setup_ui(self):
        self._main_layout = QVBoxLayout(self)
        self._create_champ_rotation_panel()
        self._create_champ_add_panel()
        self._create_champ_list_panel()
        self.setLayout(self._main_layout)
        self.setStyleSheet("background-color: #333333; color: #ffffff;")


    def _create_champ_rotation_panel(self):
        self._champ_rotation_layout = QVBoxLayout()
        self._champ_rotation_label = QLabel("test")
        self._champ_rotation_label.setAlignment(Qt.AlignCenter)
        self._champ_rotation_layout.addWidget(self._champ_rotation_label)
        self._main_layout.addLayout(self._champ_rotation_layout)

    def _create_champ_add_panel(self):
        self._champ_add_layout = QVBoxLayout()
        self._champ_add_label = QLabel("Add a champion:")
        self._champ_add_label.setAlignment(Qt.AlignCenter)
        self._champ_add_layout.addWidget(self._champ_add_label)
        self._champ_add_line_edit = QLineEdit()
        self._champ_add_layout.addWidget(self._champ_add_line_edit)
        self._main_layout.addLayout(self._champ_add_layout)

    def _create_champ_list_panel(self):
        self._champ_list_layout = QVBoxLayout()
        self._champ_list_label = QLabel("Champions you have played:")
        self._champ_list_label.setAlignment(Qt.AlignCenter)
        self._champ_list_layout.addWidget(self._champ_list_label)
        self._champ_list = QListWidget()
        self._champ_list_layout.addWidget(self._champ_list)
        self._main_layout.addLayout(self._champ_list_layout)


    @property
    def champ_rotation_label(self) -> QLabel:
        return self._champ_rotation_label
    
    @property
    def champ_add_label(self) -> QLabel:
        return self._champ_add_label
    
    @property
    def champ_add_line_edit(self) -> QLineEdit:
        return self._champ_add_line_edit
    
    @property
    def champ_list_label(self) -> QLabel:
        return self._champ_list_label
    
    @property
    def champ_list(self) -> QListWidget:
        return self._champ_list