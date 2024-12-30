from abc import ABC, abstractmethod

class ArithmeticOperation(ABC):
    """Інтерфейс для арифметичних операцій"""

    @abstractmethod
    def add(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def subtract(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def multiply(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def divide(self, a: int, b: int) -> float:
        pass