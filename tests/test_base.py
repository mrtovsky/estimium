import logging
from typing import Optional

from estimium.base import ClassLogger


class DummyClass(ClassLogger):
    """Dummy class for testing inheritance from ClassLogger."""

    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__(logger=logger)
        self.logger.info("Initializing DummyClass")

    def run(self):
        self.logger.debug("Entering `run` method")


def test_class_logging_with_getting_logger(caplog):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    dummy = DummyClass()
    dummy.run()

    assert caplog.record_tuples == [
        (
            "{}.{}".format(__name__, DummyClass.__name__),
            logging.INFO,
            "Initializing DummyClass",
        ),
        (
            "{}.{}".format(__name__, DummyClass.__name__),
            logging.DEBUG,
            "Entering `run` method",
        ),
    ]


def test_class_logging_with_specifying_logger(caplog):
    logger = logging.getLogger("foo")
    logger.setLevel(logging.DEBUG)

    dummy = DummyClass(logger=logger)
    dummy.run()

    assert caplog.record_tuples == [
        (
            "foo.{}".format(DummyClass.__name__),
            logging.INFO,
            "Initializing DummyClass",
        ),
        (
            "foo.{}".format(DummyClass.__name__),
            logging.DEBUG,
            "Entering `run` method",
        ),
    ]
