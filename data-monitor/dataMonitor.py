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

        """
        hand_position = []
        all_finger_position = []
        for hand in frame.hands:
            hand_position.append(hand.stabilized_palm_position)
            finger_position = []
            for finger in frame.fingers:
                finger_position.append(finger.stabilized_tip_position)
            all_finger_position.append(finger_position)
        """

        monitor = PrettyTable(
                ['frame_id',
                 'time_stamp',
                 'hands_count',
                 #'hand_position',
                 'fingers_count',
                 #'finger_position'
                 ])

        monitor.add_row(
                [frame.id,
                 frame.timestamp,
                 len(frame.hands),
                 #hand_position,
                 len(frame.fingers),
                 #all_finger_position
                 ])

        print monitor
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
