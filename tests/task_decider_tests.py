import unittest

from src.task import Task
from task_decider import *

class TestTaskDecider(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("Wash Dishes", 10)
        self.cook_dinner = Task("Cook Dinner", 20)
        self.clean_windows = Task("Clean Windows", 30)

    def test_task_has_description(self):
        self.assertEqual("Wash Dishes", self.wash_dishes.description)

    def test_task_has_duration(self):
        self.assertEqual(10, self.wash_dishes.duration)

    def test_gets_preferred_option_returns_wash_dishes(self):
        self.assertEqual("Wash Dishes", self.get_preferred_option.task_1)
    