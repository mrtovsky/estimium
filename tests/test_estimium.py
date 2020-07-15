"""
This module gathers tests related to the release of the new version of
Professor Estimium package.
"""


from estimium import __version__


def test_version():
    """Test version number of released package."""
    assert __version__ == "0.2.0"
