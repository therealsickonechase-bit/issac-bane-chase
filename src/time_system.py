"""
Time Management System with Wait Functionality
Copyright © 2025 Chase Allen Ringquist. All Rights Reserved.

This module implements the time management and wait functionality for the game.
"""

from enum import Enum


class TimeOfDay(Enum):
    """Represents different periods of the day."""
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    NIGHT = "night"


class TimeSystem:
    """
    Manages game time, action points, and wait functionality.
    
    Attributes:
        current_day (int): The current day number
        current_hour (int): Current hour (0-23)
        action_points (int): Remaining action points for the day
        max_action_points (int): Maximum action points per day
    """
    
    def __init__(self, max_action_points: int = 10):
        """
        Initialize the time system.
        
        Args:
            max_action_points: Maximum action points available per day
        """
        self.current_day = 1
        self.current_hour = 8  # Start at 8 AM
        self.action_points = max_action_points
        self.max_action_points = max_action_points
    
    def get_time_of_day(self) -> TimeOfDay:
        """
        Get the current time of day period.
        
        Returns:
            TimeOfDay enum representing current period
        """
        if 6 <= self.current_hour < 12:
            return TimeOfDay.MORNING
        elif 12 <= self.current_hour < 17:
            return TimeOfDay.AFTERNOON
        elif 17 <= self.current_hour < 21:
            return TimeOfDay.EVENING
        else:
            return TimeOfDay.NIGHT
    
    def wait(self, hours: int = 1) -> dict:
        """
        Wait for a specified number of hours, advancing game time.
        
        Args:
            hours: Number of hours to wait (default: 1)
        
        Returns:
            dict containing wait results with keys:
                - success (bool): Whether wait was successful
                - hours_waited (int): Actual hours waited
                - new_hour (int): New current hour
                - new_day (int): New current day
                - time_of_day (str): New time of day period
                - message (str): Description of what happened
        """
        if hours < 1:
            return {
                "success": False,
                "hours_waited": 0,
                "new_hour": self.current_hour,
                "new_day": self.current_day,
                "time_of_day": self.get_time_of_day().value,
                "message": "Cannot wait for less than 1 hour"
            }
        
        initial_hour = self.current_hour
        initial_day = self.current_day
        
        # Advance time
        self.current_hour += hours
        
        # Handle day transitions
        days_crossed = 0
        while self.current_hour >= 24:
            self.current_hour -= 24
            self.current_day += 1
            days_crossed += 1
        
        # Reset action points only once if we crossed into a new day
        if days_crossed > 0:
            self.action_points = self.max_action_points
        
        hours_passed = hours
        days_passed = self.current_day - initial_day
        
        # Generate message
        if days_passed > 0:
            message = f"You waited {hours_passed} hour(s). A new day has begun (Day {self.current_day})."
        else:
            message = f"You waited {hours_passed} hour(s). Time is now {self.current_hour}:00."
        
        return {
            "success": True,
            "hours_waited": hours_passed,
            "new_hour": self.current_hour,
            "new_day": self.current_day,
            "time_of_day": self.get_time_of_day().value,
            "message": message
        }
    
    def wait_until(self, target_hour: int) -> dict:
        """
        Wait until a specific hour of the day.
        
        Args:
            target_hour: Hour to wait until (0-23)
        
        Returns:
            dict containing wait results (same format as wait())
        """
        if not 0 <= target_hour <= 23:
            return {
                "success": False,
                "hours_waited": 0,
                "new_hour": self.current_hour,
                "new_day": self.current_day,
                "time_of_day": self.get_time_of_day().value,
                "message": "Invalid target hour. Must be between 0 and 23."
            }
        
        # Calculate hours to wait
        if target_hour > self.current_hour:
            hours_to_wait = target_hour - self.current_hour
        elif target_hour < self.current_hour:
            # Wait until next day
            hours_to_wait = (24 - self.current_hour) + target_hour
        else:
            # Already at target hour
            return {
                "success": False,
                "hours_waited": 0,
                "new_hour": self.current_hour,
                "new_day": self.current_day,
                "time_of_day": self.get_time_of_day().value,
                "message": f"Already at {target_hour}:00"
            }
        
        return self.wait(hours_to_wait)
    
    def spend_action_point(self) -> bool:
        """
        Spend one action point.
        
        Returns:
            bool: True if action point was spent, False if none available
        """
        if self.action_points > 0:
            self.action_points -= 1
            return True
        return False
    
    def get_status(self) -> dict:
        """
        Get current time system status.
        
        Returns:
            dict with current time and action point information
        """
        return {
            "day": self.current_day,
            "hour": self.current_hour,
            "time_of_day": self.get_time_of_day().value,
            "action_points": self.action_points,
            "max_action_points": self.max_action_points
        }
