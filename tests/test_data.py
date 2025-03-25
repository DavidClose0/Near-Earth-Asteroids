"""
Test data module.
"""
from unittest import TestCase
from data import get_data

class Test(TestCase):
    def test_get_data(self):
        """
        Test get_data function.
        """
        date = "2025-01-01"
        data = get_data(date)

        # Check if data contains near_earth_objects for the given date
        neos = data["near_earth_objects"][date]
        assert len(neos) > 0
        assert "id" in neos[0]

        