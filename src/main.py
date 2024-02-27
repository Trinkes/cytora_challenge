import json
import logging
import operator
import sys

from src.risk_envaluator.rules.property_evaluation_rule import (
    PropertyEvaluationRule,
)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) >= 1:
        try:
            data_to_evaluate = json.loads(arguments[0])
            logging.debug("Received dictionary: %s", data_to_evaluate)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")
    else:
        raise ValueError("No dictionary was provided")

    rule = (
        PropertyEvaluationRule("credit_rating", operator.gt, 50)
        & PropertyEvaluationRule("flood_risk", operator.lt, 10)
    ) | PropertyEvaluationRule("revenue", operator.gt, 1000000)

    logging.info(f"Evaluation result: {rule.evaluate(data_to_evaluate)}")
