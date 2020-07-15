"""Base classes to inherit from."""


import logging
from abc import ABCMeta, abstractmethod
from typing import Optional


__all__ = ["ClassLogger"]


class ClassLogger(metaclass=ABCMeta):
    """Base class for logging inside classes.

    Parameters
    ----------
    logger : object of logging.Logger, optional (default=None)
        Logging object for which a descendant class logger will be assigned.
        By default creates a new object named according to the module name
        where the object of this class was instantiated, using
        `self.__module__` name. That's why it is important to follow the
        recommended logging naming convention and name loggers using `__name__`
        special variable.

    Warnings
    --------
    This class should not be used directly. Use derived classes instead.

    It is also not suitable for being a parent class of the custom scikit-learn
    estimators because it violates the rule of not placing logic into
    instantiation. See more at `Developing scikit-learn estimators
    <https://scikit-learn.org/stable/developers/develop.html>`_.

    """

    @abstractmethod
    def __init__(self, logger: Optional[logging.Logger] = None) -> None:
        _logger = logger or logging.getLogger(self.__module__)
        self.logger = _logger.getChild(type(self).__name__)
