"""
Example usage of the Wait Functionality
Copyright © 2025 Chase Allen Ringquist. All Rights Reserved.

This demonstrates how to use the time management and wait system.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.time_system import TimeSystem


def print_status(time_system):
    """Print the current time system status."""
    status = time_system.get_status()
    print(f"\n--- Current Status ---")
    print(f"Day: {status['day']}")
    print(f"Time: {status['hour']}:00 ({status['time_of_day']})")
    print(f"Action Points: {status['action_points']}/{status['max_action_points']}")
    print("---------------------")


def main():
    """Demonstrate wait functionality."""
    print("=== Isaac Bane Chase - Wait Functionality Demo ===\n")
    
    # Initialize time system
    time_system = TimeSystem(max_action_points=10)
    
    print("Game starts on Day 1 at 8:00 AM")
    print_status(time_system)
    
    # Example 1: Wait for 1 hour
    print("\n\n=== Example 1: Wait for 1 hour ===")
    result = time_system.wait(1)
    print(f"Result: {result['message']}")
    print_status(time_system)
    
    # Example 2: Wait for multiple hours
    print("\n\n=== Example 2: Wait for 5 hours ===")
    result = time_system.wait(5)
    print(f"Result: {result['message']}")
    print_status(time_system)
    
    # Example 3: Wait until a specific time
    print("\n\n=== Example 3: Wait until 20:00 (8 PM) ===")
    result = time_system.wait_until(20)
    print(f"Result: {result['message']}")
    print_status(time_system)
    
    # Example 4: Wait across midnight
    print("\n\n=== Example 4: Wait for 10 hours (crosses into next day) ===")
    result = time_system.wait(10)
    print(f"Result: {result['message']}")
    print_status(time_system)
    
    # Example 5: Spend some action points
    print("\n\n=== Example 5: Spend action points ===")
    print("Spending 3 action points...")
    for i in range(3):
        time_system.spend_action_point()
    print_status(time_system)
    
    # Example 6: Wait to next day to reset action points
    print("\n\n=== Example 6: Wait until next day to reset action points ===")
    result = time_system.wait_until(8)
    print(f"Result: {result['message']}")
    print("Notice how action points have been restored!")
    print_status(time_system)
    
    # Example 7: Invalid wait
    print("\n\n=== Example 7: Try invalid wait (0 hours) ===")
    result = time_system.wait(0)
    print(f"Result: {result['message']}")
    print(f"Success: {result['success']}")
    
    print("\n\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
