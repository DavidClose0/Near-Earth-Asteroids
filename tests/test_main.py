"""
Test main module.
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest

class Test(TestCase):    
    def test_ui_title_and_header(self):
        """
        Test UI title and header.
        """
        at = AppTest.from_file("./app/main.py")
        at.run()

        assert at.title[0].value.startswith("Near Earth Objects")
        assert at.header[0].value.startswith("Near Earth Objects for")
        assert not at.exception