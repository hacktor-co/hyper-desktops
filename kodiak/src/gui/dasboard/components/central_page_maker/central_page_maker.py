"""
    - Created on May 24/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package create central page controller and maker
"""

from PyQt5.QtWidgets import (
    QLabel, QFrame, QFormLayout, QScrollArea,
    QVBoxLayout, QWidget
)
from PyQt5.QtCore import (
    Qt, QRect
)

from .central_page_maker_style import CentralPageMakerStyle


class CentralPageMaker(QWidget):

    def __init__(self):
        super(CentralPageMaker, self).__init__()


    def setup_ui(self, containers: QFrame, page_name: str):
        page_containers = QFrame(containers)
        page_containers.setFrameShape(QFrame.StyledPanel)
        page_containers.setFrameShadow(QFrame.Raised)
        page_containers.setObjectName("central_page_maker")
        vl_page_containers = QVBoxLayout(page_containers)
        vl_page_containers.setObjectName("vl_page_containers")

        scroll_area_page_containers = QScrollArea(page_containers)
        scroll_area_page_containers.setObjectName(CentralPageMakerStyle.scroll_area_page_containers_style[0])
        scroll_area_page_containers.setStyleSheet(CentralPageMakerStyle.scroll_area_page_containers_style[1])
        scroll_area_page_containers.setWidgetResizable(True)
        scroll_area_page_containers.setLayoutDirection(Qt.RightToLeft)
        scroll_area_contents_page_containers = QFrame()
        scroll_area_contents_page_containers.setObjectName("scroll_area_contents_page_containers")
        scroll_area_contents_page_containers.setContentsMargins(45, 45, 45, 45)

        form_base_layout = QFormLayout(scroll_area_contents_page_containers)
        form_base_layout.setContentsMargins(0, 0, 0, 0)
        form_base_layout.setHorizontalSpacing(0)
        form_base_layout.setVerticalSpacing(100)
        form_base_layout.setObjectName("form_base_layout")

        if page_name.split('-')[0] == "[TOOL]":
            from ...pages.tools.tool_page_maker import ToolPageMaker
            ToolPageMaker(
                self, form_base_layout, scroll_area_contents_page_containers
                , tool_box=page_name.split('-')[2].split(' ')[0]
            ).make_page()

        # lbl_title
        lbl_title = QLabel(scroll_area_contents_page_containers)
        lbl_title.setGeometry(QRect(441, 10, 281, 16))
        lbl_title.setObjectName(CentralPageMakerStyle.lbl_title_style[0])
        lbl_title.setStyleSheet(CentralPageMakerStyle.lbl_title_style[1])
        vl_page_containers.addWidget(scroll_area_page_containers)
        scroll_area_page_containers.setWidget(scroll_area_contents_page_containers)

        return scroll_area_page_containers
