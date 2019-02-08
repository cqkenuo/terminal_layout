# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'width = 10', width=10, back=Back.green)],
                          [TextView('', 'width = warp', width=Width.wrap, back=Back.green)],
                          [TextView('', 'width = fill', width=Width.fill, back=Back.green)],
                      ])

ctl.get_layout().width = 50

ctl.draw()
