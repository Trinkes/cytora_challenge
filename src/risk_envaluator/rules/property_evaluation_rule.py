import operator

from src.risk_envaluator.rule import Rule


class PropertyEvaluationRule(Rule):
    def __init__(
        self,
        property_name: str,
        operation: operator,
        value: int | float,
        property_not_found_value: bool = False,
    ):
        self.__property_not_found_value = property_not_found_value
        self.__value = value
        self.__operation = operation
        self.__property_name = property_name

    def evaluate(self, data: dict) -> bool:
        property_value = data.get(self.__property_name, None)
        if property_value is not None:
            try:
                return self.__operation(property_value, self.__value)
            except TypeError:
                # here we can gracefully handle the error or raise it depending on the requirement and
                # team coding standards
                return self.__property_not_found_value
        else:
            return self.__property_not_found_value
