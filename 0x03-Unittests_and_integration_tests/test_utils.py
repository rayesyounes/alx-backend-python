#!/usr/bin/env python3
"""define class TestAccessNestedMap"""

import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected_result: any) -> None:
        """Test if access_nested_map returns the expected result"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected_result: any) -> None:
        """Method to test if equal to """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, expected_exception_msg: str) -> None:
        """Method to test access_nested_map execption"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_exception_msg)


class TestGetJson(unittest.TestCase):
    """ mock requests"""

    @parameterized.expand([
        {"test_url": "http://example.com", "test_payload": {"payload": True}},
        {"test_url": "http://holberton.io", "test_payload": {"payload": False}}
    ])
    @mock.patch('utils.get_json')
    def test_get_json(self, url, mock_get_json, expected):
        """ test that utils.get_json returns the expected result. """
        mock_get_json.return_value.json.return_value = expected
        mock_get_json.assertcalledOnceWith(url)
        result = get_json(url)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
