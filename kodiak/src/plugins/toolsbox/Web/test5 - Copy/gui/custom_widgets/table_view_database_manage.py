from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import (Qt, pyqtSignal)

from ..styles.custom_widgets_styles import table_view_show_managmentdb_result
from ...tool_api_handler import execute_tool

import threading


class TableViewShowDb(QTableWidget):

    def __init__(self):
        super().__init__()

        self.setAccessibleName(table_view_show_managmentdb_result[0])
        self.setStyleSheet(table_view_show_managmentdb_result[1])

        self.setColumnCount(3)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Path"))
        self.setHorizontalHeaderItem(2, QTableWidgetItem("Language"))

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.setLayoutDirection(Qt.LeftToRight)

    def clear_all_rows(self):
        row_counter = self.rowCount()
        while self.rowCount() > 0:
            self.removeRow(row_counter)
            row_counter -= 1

    def add_result_to_display(self, item):
        try:
            if item["response"]["result"]["url"] is not None:
                row_position = self.rowCount()
                self.insertRow(row_position)

                in_comingitem = QTableWidgetItem(item["response"]["result"]["url"])
                in_comingitem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
                self.setItem(row_position, 0, in_comingitem)

                in_comingitem = QTableWidgetItem(str(item["response"]["result"]["code"]))
                in_comingitem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
                self.setItem(row_position, 1, in_comingitem)
        except Exception:
            pass

    def set_data(self):
        # TODO: fix this section of code for handling the thread executors
        thread = threading.Thread(target=self.__execute_display_result__)
        thread.start()
