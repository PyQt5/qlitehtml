#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2024/07/09
@author: Irony
@site: https://pyqt.site | https://github.com/PyQt5
@email: 892768447@qq.com
@file: markdown.py
@description:
"""

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append("../../dist")

import markdown
from PyQt5.QLiteHtmlWidget import QLiteHtmlWidget
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMenu,
    QMessageBox,
    QSplitter,
    QTextEdit,
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._changeTimer = QTimer(self)
        self._changeTimer.setSingleShot(True)
        self._changeTimer.timeout.connect(self.onChange)

        self._menu = QMenu("File", self)
        self._menu.addAction("Open", self.openFile)
        self.menuBar().addMenu(self._menu)

        self._mainWidget = QSplitter(Qt.Horizontal, self)
        self._textEdit = QTextEdit(self._mainWidget)
        # 1s
        self._textEdit.textChanged.connect(lambda: self._changeTimer.start(1000))
        self._htmlWidget = QLiteHtmlWidget(self._mainWidget)

        self._mainWidget.addWidget(self._textEdit)
        self._mainWidget.addWidget(self._htmlWidget)
        self.setCentralWidget(self._mainWidget)
        self._htmlWidget.setResourceHandler(self.onHandler)

    def onHandler(self, url):
        print(url)
        return b""

    def sizeHint(self):
        return QSize(800, 600)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open Markdown File", "", "Markdown Files (*.md)"
        )
        if fileName:
            self.setWindowTitle(fileName)
            os.chdir(os.path.dirname(fileName))
            try:
                with open(fileName, "r", encoding="utf-8") as f:
                    self._textEdit.setPlainText(f.read())
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def onChange(self):
        text = self._textEdit.toPlainText().strip()
        if len(text) == 0:
            return
        try:
            html = markdown.markdown(text)
            self._htmlWidget.setHtml(html)
        except Exception as e:
            print(e)
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
