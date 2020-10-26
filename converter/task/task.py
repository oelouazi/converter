from abc import ABC, abstractmethod


class Task(ABC):
    """
    Represents an abstract task runnable in a thread.
    """

    @abstractmethod
    def run(self):
        """
        Run logic to execute in a thread.
        """
        pass
