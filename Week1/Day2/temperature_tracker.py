import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        self.temps = [0] * 111
        self.num_temps = 0
        self.min = 111
        self.max = -1
        self.total = 0
        self.mean = None
        self.max_freq = 0
        self.mode = None

    def insert(self, temperature):
        if temperature < 0 or temperature > 110:
            raise Exception
        self.temps[temperature] += 1
        # print(temperature)
        self.num_temps += 1
        if temperature < self.min:
            self.min = temperature
        if temperature > self.max:
            self.max = temperature
        self.total += temperature
        self.mean = self.total / float(self.num_temps)
        if self.temps[temperature] > self.max_freq:
            self.max_freq = self.temps[temperature]
            self.mode = temperature

    def get_max(self):
        max = self.max
        if max == -1:
            max = None
        return max

    def get_min(self):
        min = self.min
        if min == 111:
            min = None
        return min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

    







# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        # print(tracker.get_max(), 80, msg,"=",'max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)
        
        tracker.insert(20)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 20, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 52.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)