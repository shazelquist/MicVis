"""
    This module defines the update methods for animations on diferent types of output
"""
from audio_capture import *
from gui_disp import *


def ani_bar(arg):
    """
        Defines output method for updating bar plot
    """
    readstream()
    ax1.clear()
    ax1.bar(0, amprec[-1])


def ani_plot(arg):
    """
        Defines output method for updating line plot
    """
    readstream()
    ax1.clear()
    ax1.plot(timerec, amprec)
    ax1.scatter(timerec[-1], amprec[-1])


# management dictionary for selecting the correct function
ani_reference = {"bar": ani_bar, "plot": ani_plot}
