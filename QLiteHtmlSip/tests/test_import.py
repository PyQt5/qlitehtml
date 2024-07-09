#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2024/07/09
@author: Irony
@site: https://pyqt.site | https://github.com/PyQt5
@email: 892768447@qq.com
@file: test.py
@description:
"""

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append("../../dist")


from PyQt5.QLiteHtmlWidget import QLiteHtmlWidget

print(dir(QLiteHtmlWidget))
