import unittest

from src.task_decider import task_decider

class TestTaskDecider(unittest.TestCase):

    def test_task_decider_returns_wash_dishes(self):
        self.assertEqual("Wash Dishes", return_wash_dishes(name))
