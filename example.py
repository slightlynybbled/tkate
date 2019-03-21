import logging
from random import random, choice
from time import sleep
import tkinter as tk

from ate import Test
from ate import TestSequence
from tkate import TkAteFrame


# The CommunicationTest class shows the minimum test structure that might be reasonably
# be implemented.  Only the `execute()` method is implemented.
class CommunicationTest(Test):
    def __init__(self, loglevel=logging.INFO):
        super().__init__(moniker='communications test', loglevel=loglevel)

    # overriding the execute method
    def execute(self, aborted=False):
        # a normal test would set `test_is_passing` based on real conditions, we
        # are implementing a random value here simply for illustrative purposes
        passing = choice([True] * 3 + [False])

        if not passing:
            self.fail()

        # should return a (key, value) which are the results of the test
        return passing


# The PumpFlowTest implements the `setup' and `teardown` methods as well in order to demonstrate what that may look like
class PumpFlowTest(Test):
    def __init__(self, loglevel=logging.INFO):
        super().__init__(moniker='pump flow test', loglevel=loglevel)

    def setup(self, aborted=False):
        # setting the speed of the pump might be something done in the setup, including
        # the wait time to speed up the pump, which we will simulate with a 2s sleep
        sleep(2.0)

    def execute(self, aborted=False):
        # user may abort the test based on the `aborted` or may
        # continue the test, at the author's discretion
        if aborted:
            return None

        # simulate long-running process, such as several flow measurement/averaging cycles
        sleep(0.1)
        flow = 5.5 + random()

        # apply conditions, fail the test if outside of those conditions
        if not 5.6 <= flow <= 6.4:
            self.fail()

        # should return a (key, value) tuple which are the results of the test
        return flow

    def teardown(self, aborted=False):
        # again, simulating another long-running process...
        sleep(0.1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # create the sequence of test objects
    sequence = [CommunicationTest(), PumpFlowTest()]
    ts = TestSequence(sequence=sequence, auto_run=False, loglevel=logging.DEBUG)

    window = tk.Tk()

    tkate_frame = TkAteFrame(window, ts)
    tkate_frame.grid()

    window.mainloop()
