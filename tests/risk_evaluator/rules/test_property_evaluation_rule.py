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

    def test_chained_rules(self):
        rule = PropertyEvaluationRule(
            property_name="age", operation=operator.lt, value=10
        ) & PropertyEvaluationRule(
            property_name="height", operation=operator.le, value=5
        ) | (
            PropertyEvaluationRule(
                property_name="height", operation=operator.gt, value=10
            )
            & PropertyEvaluationRule(
                property_name="age", operation=operator.gt, value=20
            )
        )
        self.assertTrue(rule.evaluate({"age": 5, "height": 5}))
        self.assertTrue(rule.evaluate({"age": 22, "height": 11}))

        rule = (
            PropertyEvaluationRule(
                property_name="age", operation=operator.lt, value=10
            )  #
            | PropertyEvaluationRule(
                property_name="height", operation=operator.le, value=5
            )  # F
        ) & (
            PropertyEvaluationRule(
                property_name="height", operation=operator.gt, value=10
            )
            | PropertyEvaluationRule(
                property_name="age", operation=operator.gt, value=20
            )
        )  # F
        self.assertFalse(rule.evaluate({"age": 5, "height": 5}))
        self.assertFalse(rule.evaluate({"age": 22, "height": 11}))
        self.assertTrue(rule.evaluate({"age": 22, "height": 1}))
