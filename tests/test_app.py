"""
Test main module.
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest

class Test(TestCase):    
    def test_ui_title_and_header(self):
        """
        Test UI sidebar title and header.
        """
        at = AppTest.from_file("./src/app.py", default_timeout=30)
        at.run()

        # Check if sidebar title and header are correct
        assert at.title[0].value == "Navigation"
        assert at.header[0].value.startswith("Near Earth Objects for")
        assert not at.exception