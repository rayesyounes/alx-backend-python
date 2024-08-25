#!/usr/bin/env python3
"""define class TestAccessNestedMap"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test if access_nested_map returns the expected result"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
