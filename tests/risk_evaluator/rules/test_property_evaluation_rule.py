import operator
from unittest import TestCase

from src.risk_envaluator.rules.property_evaluation_rule import PropertyEvaluationRule


class TestPropertyEvaluation(TestCase):
    def setUp(self):
        self.rule = PropertyEvaluationRule(
            property_name="test_field", operation=operator.gt, value=10
        )

    def test_evaluate(self):
        rule = PropertyEvaluationRule(
            property_name="test_field", operation=operator.gt, value=10
        )
        self.assertTrue(rule.evaluate({"test_field": 75}))

    def test_evaluate_absent_value(self):
        rule = PropertyEvaluationRule(
            property_name="test_field",
            operation=operator.gt,
            value=10,
            property_not_found_value=True,
        )
        self.assertTrue(rule.evaluate({"test_field2": 75}))

    def test_evaluate_invalid_value(self):
        rule = PropertyEvaluationRule(
            property_name="test_field",
            operation=operator.gt,
            value=10,
            property_not_found_value=False,
        )
        self.assertFalse(rule.evaluate({"test_field": "7"}))
