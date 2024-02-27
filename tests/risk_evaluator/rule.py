import unittest
from unittest.mock import Mock

from src.risk_envaluator.rule import OrRule, Rule, AndRule


class TestOrRule(unittest.TestCase):
    def setUp(self):
        self.data = {"test_field": "test_data"}
        self.rule1 = Mock(spec=Rule)
        self.rule2 = Mock(spec=Rule)

    def test_rule_1_true(self):
        self.rule1.evaluate.return_value = True
        self.rule2.evaluate.return_value = False

        test_rule = OrRule(self.rule1, self.rule2)
        result = test_rule.evaluate(self.data)
        self.assertTrue(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_not_called()

    def test_rule_2_true(self):
        test_rule = OrRule(self.rule1, self.rule2)

        self.rule1.evaluate.return_value = False
        self.rule2.evaluate.return_value = True
        result = test_rule.evaluate(self.data)
        self.assertTrue(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_called_with(self.data)

    def test_all_false(self):
        test_rule = OrRule(self.rule1, self.rule2)

        self.rule1.evaluate.return_value = False
        self.rule2.evaluate.return_value = False
        result = test_rule.evaluate(self.data)
        self.assertFalse(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_called_with(self.data)

    def test_all_true(self):
        test_rule = OrRule(self.rule1, self.rule2)

        self.rule1.evaluate.return_value = True
        self.rule2.evaluate.return_value = True
        result = test_rule.evaluate(self.data)
        self.assertTrue(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_not_called()


class TestAndRule(unittest.TestCase):
    def setUp(self):
        self.data = {"test_field": "test_data"}
        self.rule1 = Mock(spec=Rule)
        self.rule2 = Mock(spec=Rule)

    def test_rule_1_true(self):
        self.rule1.evaluate.return_value = True
        self.rule2.evaluate.return_value = False

        test_rule = AndRule(self.rule1, self.rule2)
        result = test_rule.evaluate(self.data)
        self.assertFalse(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_called_with(self.data)

    def test_rule_2_true(self):
        self.rule1.evaluate.return_value = False
        self.rule2.evaluate.return_value = True

        test_rule = AndRule(self.rule1, self.rule2)
        result = test_rule.evaluate(self.data)
        self.assertFalse(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_not_called()

    def test_both_true(self):
        self.rule1.evaluate.return_value = True
        self.rule2.evaluate.return_value = True

        test_rule = AndRule(self.rule1, self.rule2)
        result = test_rule.evaluate(self.data)
        self.assertTrue(result)
        self.rule1.evaluate.assert_called_with(self.data)
        self.rule2.evaluate.assert_called_with(self.data)
