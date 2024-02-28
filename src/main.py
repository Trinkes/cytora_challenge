import json
import logging
import operator
import sys

from src.evaluate_risk_usecase import EvaluateRiskUsecase
from src.risk_envaluator.rules.property_evaluation_rule import (
    NumberPropertyEvaluationRule,
)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    input_dictionary_info = """
        The dictionary should contain the following keys:
        - credit_rating
        - flood_risk
        - revenue

        The dictionary values should be numbers.

        > :warning: you must escape the json string
        
        example:
        docker run cytora "{\\\"credit_rating\\\":75,\\\"flood_risk\\\":5,\\\"revenue\\\":1000}"
    """
    if len(arguments) >= 1:
        try:
            data_to_evaluate = json.loads(arguments[0])
            logging.debug("Received dictionary: %s", data_to_evaluate)
        except json.JSONDecodeError as e:
            logging.error("Cannot load the dictionary. \n" + input_dictionary_info)
            exit(1)
    else:
        logging.error("No dictionary provided. \n" + input_dictionary_info)
        exit(1)

    risk_usecase = EvaluateRiskUsecase()
    risk_usecase.evaluate_risk(data_to_evaluate)

    logging.info(f"Evaluation result: {risk_usecase.evaluate_risk(data_to_evaluate)}")
