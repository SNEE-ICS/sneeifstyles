# QUANTUMBLACK CONFIDENTIAL
#
# Copyright (c) 2016 - present QuantumBlack Visual Analytics Ltd. All
# Rights Reserved.
#
# NOTICE: All information contained herein is, and remains the property of
# QuantumBlack Visual Analytics Ltd. and its suppliers, if any. The
# intellectual and technical concepts contained herein are proprietary to
# QuantumBlack Visual Analytics Ltd. and its suppliers and may be covered
# by UK and Foreign Patents, patents in process, and are protected by trade
# secret or copyright law. Dissemination of this information or
# reproduction of this material is strictly forbidden unless prior written
# permission is obtained from QuantumBlack Visual Analytics Ltd.

"""
This module contains the ``mpl_style`` function which applies the QB ``matplotlib`` theme

Some of the tick properties cannot be set using ``plt.style.use``,
so we have to set them in code.

We want the user to be able to apply the full style, including styling the
minor ticks, using only a _single_ function call. To make this possible we need
to monkey patch as we first need to apply the style using ``plt.style.use``,
then create a figure (using either ``plt.figure`` or ``plt.Figure`` or
``plt.subplots``), and _then_ get from this figure the axes to style the ticks.
"""
import matplotlib.pyplot as plt
import matplotlib.axes
from os.path import join, dirname, realpath

STYLE_DIR = realpath(join(dirname(__file__), "styles"))
COMMON_STYLE = "qb-common.mplstyle"

__all__ = ["mpl_style"]

original_subplots = plt.subplots
original_figure = plt.figure

def mpl_style():

    plt.style.use(join(STYLE_DIR, COMMON_STYLE))

