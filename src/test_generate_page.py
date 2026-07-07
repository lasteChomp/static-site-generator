import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = "# The Last Airbender"
        title = extract_title(md)
        self.assertEqual("The Last Airbender", title)

    def test_extract_title_multilines(self):
        md = """
### This is not a h1 title but a h3 title

## This is not a h1 title but a h2 title

# This is indeed a h1 title

## This is the second h2 title

### This is the second h3 title

# This is the second h1 title
"""
        title = extract_title(md)
        self.assertEqual("This is indeed a h1 title", title)