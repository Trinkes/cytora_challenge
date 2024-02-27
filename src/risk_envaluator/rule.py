import abc
from abc import abstractmethod


class Rule(abc.ABC):
    @abstractmethod
    def evaluate(self, data: dict[str, int]) -> bool:
        pass

    def __or__(self, other) -> "Rule":
        return OrRule(self, other)

    def __and__(self, other) -> "Rule":
        return AndRule(self, other)


class OrRule(Rule):
    def __init__(self, rule1: Rule, rule2: Rule):
        self.rule1 = rule1
        self.rule2 = rule2

    def evaluate(self, data: dict[str, int]) -> bool:
        return self.rule1.evaluate(data) or self.rule2.evaluate(data)


class AndRule(Rule):
    def __init__(self, rule1: Rule, rule2: Rule):
        self.rule1 = rule1
        self.rule2 = rule2

    def evaluate(self, data: dict[str, int]) -> bool:
        return self.rule1.evaluate(data) and self.rule2.evaluate(data)
