import os, sys, time, inspect
from prettytable import PrettyTable

"""
#Environment Setup

@src_dir  : file current path
@arch_dir : libs path of different architecture
@leap_dir : Leap Motion module path
"""
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../../motion-leap/lib/x64' if sys.maxsize > 2 ** 32 else '../../motion-leap/lib/x86'
leap_dir = '../../motion-leap/lib'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))
import Leap


class Listener(Leap.Listener):
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()
        hand = frame.hands.rightmost
        interaction_box = frame.interaction_box
        palm_position = hand.stabilized_palm_position
        normalized_palm = interaction_box.normalize_point(palm_position)
        x = normalized_palm.x * 16 - 1
        y = (1 - normalized_palm.y) * 9 - 1

        print '-------------------------------------------------------------->x:', normalized_palm.x
        print '-------------------------------------------------------------->y:', 1 - normalized_palm.y

        window = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]
        window[int(y)][int(x)] = '+'
        for y in window:
            print y

        time.sleep(0.1)
        os.system('clear')


def main():
    listener = Listener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
