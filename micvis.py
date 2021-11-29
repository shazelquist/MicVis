"""
    MicVisualizer core file that runs proccesses for session.
"""
import audio_capture
import gui_disp
import animations

displaymode = "plot"


def run_display():
    """
        Performs generic setup for 
    """
    ani = gui_disp.animation.FuncAnimation(
        gui_disp.fig, animations.ani_reference[displaymode], interval=1
    )
    gui_disp.plt.show()  # show the plot


def main():
    """
        Runs applicaiton given current configuration
    """
    audio_capture.openstream()
    run_display()
    audio_capture.endstream()


if __name__ == "__main__":
    main()
