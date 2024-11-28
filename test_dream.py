#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bonita McBride
CS 521 - Fall 1
October 13, 2024
Final Project - Dream Log - Unit Test 
"""

import unittest
from dream import Dream

class TestDreamMethods(unittest.TestCase):

    def setUp(self):
        # create dreams to test
        self.dream1 = Dream("2024-10-12",
                            "I ate a 100 pound burger and then blew up.", 
                            ["Nightmare"])
        self.dream2 = Dream("2024-10-13", 
                            "Hamsters were jumping on a trampoline", 
                            ["Funny"])
        self.dream3 = Dream("2024-10-14", 
                            "Lost control of car and drove off bridge", 
                            ["Nightmare"])
        self.dream4 = Dream("2024-10-14", 
                            "Bought a new car.", 
                            ["Happy"])
        self.dreams = [self.dream1, self.dream2, self.dream3, self.dream4]

    def test_keyword_search(self):
        # test 1: check if keyword search gets the right dreams
        keyword = "car"
        result = [dream for dream in self.dreams if keyword in dream]
        
        self.assertIn(self.dream3, result, f"Test failed: n\
                      Expected to find dream with keyword '{keyword}'")
        self.assertIn(self.dream4, result, f"Test failed: n\
                      Expected to find dream with keyword '{keyword}'")

    def test_dream_type_filter(self):
        # test 2: check to see if dream type grabs the right dreams
        dream_type = "Nightmare"
        filtered_dreams = [dream for dream in self.dreams if dream_type in dream.types]
        
        self.assertIn(self.dream1, filtered_dreams, f"Test failed: n\
                      Expected to find dream of type '{dream_type}'")
        self.assertIn(self.dream3, filtered_dreams, f"Test failed: n\
                      Expected to find dream of type '{dream_type}'")
        self.assertEqual(len(filtered_dreams), 2, f"Test failed: n\
                         Expected two dreams of type '{dream_type}'")

if __name__ == '__main__':
    unittest.main()




