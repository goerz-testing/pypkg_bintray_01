"""Tests for `pypkg_bintray_01` package."""

import pytest
from pkg_resources import parse_version

import pypkg_bintray_01


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(pypkg_bintray_01.__version__)
    v_orig = parse_version("0.0.1-dev")
    assert v_curr >= v_orig
