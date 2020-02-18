"""
This file demonstrates how one might "trigger" a test sequence start by simply
starting and running the test sequence using the TestSequence.start() method
bound to the <Tab> event.
"""

import logging
from random import random, choice
from time import sleep
import tkinter as tk

from mats import Test
from mats import TestSequence
from tkmats import TkMatsFrame


# The CommunicationTest class shows the minimum test structure that might
# be reasonably be implemented.  Only the `execute()` method is implemented.
class CommunicationTest(Test):
    def __init__(self, loglevel=logging.INFO):
        super().__init__(moniker='communications test',
                         pass_if=True,
                         loglevel=loglevel)

    # overriding the execute method
    def execute(self, is_passing):
        # a normal test would set `test_is_passing` based on real conditions,
        # we are implementing a random value here simply for illustrative
        # purposes
        passing = choice([True] * 3 + [False])

        # should return a (key, value) which are the results of the test
        return passing


# The PumpFlowTest implements the `setup' and `teardown` methods as well
# in order to demonstrate what that may look like
class PumpFlowTest(Test):
    def __init__(self, loglevel=logging.INFO):
        super().__init__(moniker='pump flow test',
                         min_value=5.6, max_value=6.4,
                         loglevel=loglevel)

    def setup(self, is_passing):
        # setting the speed of the pump might be something done in the setup,
        # including the wait time to speed up the pump, which we will
        # simulate with a 2s sleep
        sleep(2.0)

    def execute(self, is_passing):
        # simulate long-running process, such as
        # several flow measurement/averaging cycles
        sleep(0.1)
        flow = 5.5 + random()

        # should return a (key, value) tuple which are the results of the test
        return flow

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # create the sequence of test objects
    sequence = [CommunicationTest(), PumpFlowTest()]
    ts = TestSequence(sequence=sequence, auto_run=False, loglevel=logging.DEBUG)

    window = tk.Tk()

    tk.Label(window,
             text='Click into the Entry and press "Tab" to begin the test')\
        .grid(row=0, column=0)

    entry = tk.Entry(window)
    entry.grid(row=1, column=0)

    entry.bind('<Tab>', lambda _: ts.start())

    tkate_frame = TkMatsFrame(window, ts, vertical=True, start_btn=False)
    tkate_frame.grid(row=2, column=0)

    window.mainloop()
