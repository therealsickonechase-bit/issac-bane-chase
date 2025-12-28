"""
Tests for Time Management System and Wait Functionality
Copyright © 2025 Chase Allen Ringquist. All Rights Reserved.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.time_system import TimeSystem, TimeOfDay


class TestTimeSystem(unittest.TestCase):
    """Test cases for TimeSystem class."""
    
    def setUp(self):
        """Set up a fresh TimeSystem for each test."""
        self.time_system = TimeSystem(max_action_points=10)
    
    def test_initialization(self):
        """Test that TimeSystem initializes correctly."""
        self.assertEqual(self.time_system.current_day, 1)
        self.assertEqual(self.time_system.current_hour, 8)
        self.assertEqual(self.time_system.action_points, 10)
        self.assertEqual(self.time_system.max_action_points, 10)
    
    def test_get_time_of_day_morning(self):
        """Test time of day detection for morning."""
        self.time_system.current_hour = 8
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.MORNING)
        
        self.time_system.current_hour = 6
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.MORNING)
        
        self.time_system.current_hour = 11
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.MORNING)
    
    def test_get_time_of_day_afternoon(self):
        """Test time of day detection for afternoon."""
        self.time_system.current_hour = 12
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.AFTERNOON)
        
        self.time_system.current_hour = 14
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.AFTERNOON)
        
        self.time_system.current_hour = 16
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.AFTERNOON)
    
    def test_get_time_of_day_evening(self):
        """Test time of day detection for evening."""
        self.time_system.current_hour = 17
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.EVENING)
        
        self.time_system.current_hour = 19
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.EVENING)
        
        self.time_system.current_hour = 20
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.EVENING)
    
    def test_get_time_of_day_night(self):
        """Test time of day detection for night."""
        self.time_system.current_hour = 21
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.NIGHT)
        
        self.time_system.current_hour = 23
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.NIGHT)
        
        self.time_system.current_hour = 0
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.NIGHT)
        
        self.time_system.current_hour = 5
        self.assertEqual(self.time_system.get_time_of_day(), TimeOfDay.NIGHT)
    
    def test_wait_basic(self):
        """Test basic wait functionality."""
        result = self.time_system.wait(1)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 1)
        self.assertEqual(result["new_hour"], 9)
        self.assertEqual(result["new_day"], 1)
        self.assertEqual(self.time_system.current_hour, 9)
    
    def test_wait_multiple_hours(self):
        """Test waiting multiple hours."""
        result = self.time_system.wait(5)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 5)
        self.assertEqual(result["new_hour"], 13)
        self.assertEqual(self.time_system.current_hour, 13)
    
    def test_wait_across_midnight(self):
        """Test waiting that crosses midnight into a new day."""
        self.time_system.current_hour = 22
        result = self.time_system.wait(4)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 4)
        self.assertEqual(result["new_hour"], 2)
        self.assertEqual(result["new_day"], 2)
        self.assertEqual(self.time_system.current_day, 2)
    
    def test_wait_full_day(self):
        """Test waiting for a full day."""
        result = self.time_system.wait(24)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 24)
        self.assertEqual(result["new_hour"], 8)
        self.assertEqual(result["new_day"], 2)
    
    def test_wait_multiple_days(self):
        """Test waiting across multiple days."""
        result = self.time_system.wait(50)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 50)
        self.assertEqual(result["new_hour"], 10)  # 8 + 50 = 58, 58 % 24 = 10
        self.assertEqual(result["new_day"], 3)  # Day 1 + 2 days = Day 3
    
    def test_wait_invalid_hours(self):
        """Test waiting with invalid hour values."""
        result = self.time_system.wait(0)
        
        self.assertFalse(result["success"])
        self.assertEqual(result["hours_waited"], 0)
        self.assertEqual(self.time_system.current_hour, 8)
        
        result = self.time_system.wait(-5)
        self.assertFalse(result["success"])
    
    def test_wait_resets_action_points(self):
        """Test that action points reset when crossing into a new day."""
        self.time_system.action_points = 3
        self.time_system.current_hour = 22
        
        result = self.time_system.wait(4)
        
        self.assertTrue(result["success"])
        self.assertEqual(self.time_system.action_points, 10)  # Reset to max
        self.assertEqual(self.time_system.current_day, 2)
    
    def test_wait_until_future_time(self):
        """Test waiting until a future time same day."""
        self.time_system.current_hour = 10
        result = self.time_system.wait_until(15)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 5)
        self.assertEqual(result["new_hour"], 15)
        self.assertEqual(result["new_day"], 1)
    
    def test_wait_until_next_day(self):
        """Test waiting until a time that requires going to next day."""
        self.time_system.current_hour = 20
        result = self.time_system.wait_until(8)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["hours_waited"], 12)  # 4 hours to midnight + 8 hours
        self.assertEqual(result["new_hour"], 8)
        self.assertEqual(result["new_day"], 2)
    
    def test_wait_until_same_hour(self):
        """Test waiting until the current hour (should fail)."""
        self.time_system.current_hour = 10
        result = self.time_system.wait_until(10)
        
        self.assertFalse(result["success"])
        self.assertEqual(result["hours_waited"], 0)
        self.assertIn("Already at", result["message"])
    
    def test_wait_until_invalid_hour(self):
        """Test waiting until an invalid hour."""
        result = self.time_system.wait_until(25)
        
        self.assertFalse(result["success"])
        self.assertIn("Invalid target hour", result["message"])
        
        result = self.time_system.wait_until(-1)
        self.assertFalse(result["success"])
    
    def test_spend_action_point(self):
        """Test spending action points."""
        initial_ap = self.time_system.action_points
        
        success = self.time_system.spend_action_point()
        
        self.assertTrue(success)
        self.assertEqual(self.time_system.action_points, initial_ap - 1)
    
    def test_spend_action_point_depleted(self):
        """Test spending action points when none available."""
        self.time_system.action_points = 0
        
        success = self.time_system.spend_action_point()
        
        self.assertFalse(success)
        self.assertEqual(self.time_system.action_points, 0)
    
    def test_get_status(self):
        """Test getting time system status."""
        status = self.time_system.get_status()
        
        self.assertEqual(status["day"], 1)
        self.assertEqual(status["hour"], 8)
        self.assertEqual(status["time_of_day"], "morning")
        self.assertEqual(status["action_points"], 10)
        self.assertEqual(status["max_action_points"], 10)
    
    def test_get_status_after_wait(self):
        """Test status after waiting."""
        self.time_system.wait(5)
        status = self.time_system.get_status()
        
        self.assertEqual(status["day"], 1)
        self.assertEqual(status["hour"], 13)
        self.assertEqual(status["time_of_day"], "afternoon")


if __name__ == '__main__':
    unittest.main()
