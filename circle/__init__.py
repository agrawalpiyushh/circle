"""
circle
A demo project for APS Hack Day 2019
"""

# Add imports here
from .circle import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
