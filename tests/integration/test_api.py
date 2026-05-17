import json
import unittest
from unittest.mock import MagicMock, patch

from src.api_client import search_books


MOCK_RESPONSE = {
    "numFound": 2,
    "docs": [
        {
            "title": "Learning Python",
            "author_name": ["Mark Lutz"],
            "first_publish_year": 2013,
        },
        {
            "title": "Python Cookbook",
            "author_name": ["David Beazley", "Brian K. Jones"],
            "first_publish_year": 2013,
        },
    ],
}


class TestSearchBooks(unittest.TestCase):
    @patch("src.api_client.urllib.request.urlopen")
    def test_returns_parsed_books(self, mock_urlopen):
        body = json.dumps(MOCK_RESPONSE).encode("utf-8")
        cm = MagicMock()
        cm.__enter__ = MagicMock(return_value=MagicMock(read=MagicMock(return_value=body)))
        cm.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = cm

        books = search_books("python")

        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]["title"], "Learning Python")
        self.assertEqual(books[0]["authors"], ["Mark Lutz"])
        self.assertEqual(books[0]["year"], 2013)

    @patch("src.api_client.urllib.request.urlopen")
    def test_encodes_query_in_url(self, mock_urlopen):
        body = json.dumps({"docs": []}).encode("utf-8")
        cm = MagicMock()
        cm.__enter__ = MagicMock(return_value=MagicMock(read=MagicMock(return_value=body)))
        cm.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = cm

        search_books("machine learning")

        called_url = mock_urlopen.call_args[0][0]
        self.assertIn("machine%20learning", called_url)

    @patch("src.api_client.urllib.request.urlopen")
    def test_connection_error_raises_connection_error(self, mock_urlopen):
        mock_urlopen.side_effect = OSError("Network unreachable")

        with self.assertRaises(ConnectionError):
            search_books("python")

    @patch("src.api_client.urllib.request.urlopen")
    def test_empty_results(self, mock_urlopen):
        body = json.dumps({"docs": []}).encode("utf-8")
        cm = MagicMock()
        cm.__enter__ = MagicMock(return_value=MagicMock(read=MagicMock(return_value=body)))
        cm.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = cm

        books = search_books("xyzxyzxyz")

        self.assertEqual(books, [])


if __name__ == "__main__":
    unittest.main()
