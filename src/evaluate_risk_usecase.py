import operator

from src.risk_envaluator.rules.property_evaluation_rule import (
    NumberPropertyEvaluationRule,
)


class EvaluateRiskUsecase:
    def evaluate_risk(self, data: dict[str, int]) -> bool:
        rule = (
            NumberPropertyEvaluationRule("credit_rating", operator.gt, 50)
            & NumberPropertyEvaluationRule("flood_risk", operator.lt, 10)
        ) | NumberPropertyEvaluationRule("revenue", operator.gt, 1000000)
        return rule.evaluate(data)
