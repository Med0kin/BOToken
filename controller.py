from view import Window
from model import Model
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys

class Controller():


    def __init__(self, view: Window, model: Model) -> None:
        self._view = view
        self._model = model
        self._connect_signals()
        self._update_list()


    def _connect_signals(self) -> None:
        line_edit = self._view.champ_add_line_edit
        line_edit.returnPressed.connect(self._add_champion) # type: ignore
        self._view.champ_list.keyPressEvent = self._handle_key_press

    def _add_champion(self) -> None:
        line_edit = self._view.champ_add_line_edit
        champion_name = line_edit.text().strip().title()
        if champion_name not in self._model.all_champions:
            self._view.champ_add_label.setText(f"{champion_name} is not a champion")
            raise ValueError(f"Champion {champion_name} not in list of all champions.")
        if champion_name in self._model.champions:
            self._view.champ_add_label.setText(f"{champion_name} already in list")
            raise ValueError(f"Champion {champion_name} already in list of played champions.")
        self._model.champions.append(champion_name)
        self._model.save_to_file()
        line_edit.clear()
        self._update_list()
        self._view.champ_add_label.setText(f"{champion_name} added")

    def _handle_key_press(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Delete:
            if self._view.champ_list.hasFocus():
                self._remove_champion(self._view.champ_list.currentItem().text())
                self._update_list()

    def _remove_champion(self, champion_name: str) -> None:
        champions = self._model.champions
        if champion_name not in champions:
            self._view.champ_add_label.setText(f"{champion_name} could not be removed")
            raise ValueError(f"Champion {champion_name} not in list of played champions.")
        self._model.champions.remove(champion_name)
        self._model.save_to_file()
        self._view.champ_add_label.setText(f"{champion_name} removed")
        
    def _update_list(self) -> None:
        # rotation label
        text = ""
        for champion in self._model.champions_in_rotation:
            if champion in self._model.champions:
                text += f"<font color=\"green\">{champion}</font> "
            else:
                text += f"<font color=\"red\">{champion}</font> "
        self._view.champ_rotation_label.setText(text)
        # add label
        self._view.champ_list_label.setText(f"{len(self._model.champions)}/{len(self._model.all_champions)}")
        # list
        champ_list = self._view.champ_list
        champ_list.clear()
        for champion in self._model.champions:
            # Add champion to list with green background
            item = QListWidgetItem(champion)
            item.setBackground(QColor(0, 200, 0))
            item.setForeground(QColor(0, 0, 0))
            champ_list.addItem(item)
        champ_list.sortItems()
        for champion in self._model.all_champions:
            if champion not in self._model.champions:
                # Add champion to list with red background
                item = QListWidgetItem(champion)
                item.setBackground(QColor(200, 0, 0))
                item.setForeground(QColor(0, 0, 0))
                champ_list.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Window()
    model = Model()
    controller = Controller(view, model)
    sys.exit(app.exec_())