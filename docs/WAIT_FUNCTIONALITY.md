# Wait Functionality Documentation

**Copyright © 2025 Chase Allen Ringquist. All Rights Reserved.**

## Overview

The Wait Functionality is a core time management system for Isaac Bane Chase that allows the game to track time, manage daily cycles, and provide players with the ability to wait or pass time.

## Features

### Time System

The `TimeSystem` class manages:
- **Current time** (day number and hour of day)
- **Time of day periods** (morning, afternoon, evening, night)
- **Action points** (daily resource that resets each new day)
- **Wait functionality** (advance time by hours or to specific times)

### Wait Actions

#### Basic Wait
Wait for a specified number of hours:
```python
from src.time_system import TimeSystem

time_system = TimeSystem()
result = time_system.wait(5)  # Wait for 5 hours
```

#### Wait Until
Wait until a specific hour of the day:
```python
result = time_system.wait_until(20)  # Wait until 8 PM (20:00)
```

### Time of Day

The system automatically tracks four periods:
- **Morning**: 6:00 - 11:59
- **Afternoon**: 12:00 - 16:59
- **Evening**: 17:00 - 20:59
- **Night**: 21:00 - 5:59

### Action Points

- Players start with 10 action points per day (configurable)
- Action points can be spent on various activities
- Action points automatically reset to maximum when a new day begins
- Crossing midnight during a wait will trigger the reset

## API Reference

### TimeSystem Class

#### Constructor
```python
TimeSystem(max_action_points: int = 10)
```
Creates a new time system instance.

#### Methods

**wait(hours: int = 1) -> dict**
- Wait for a specified number of hours
- Returns a dict with:
  - `success`: Whether the wait was successful
  - `hours_waited`: Number of hours actually waited
  - `new_hour`: Current hour after waiting
  - `new_day`: Current day number after waiting
  - `time_of_day`: Current time period
  - `message`: Description of what happened

**wait_until(target_hour: int) -> dict**
- Wait until a specific hour (0-23)
- Returns same format as `wait()`

**spend_action_point() -> bool**
- Spend one action point
- Returns True if successful, False if no points available

**get_status() -> dict**
- Get current time system status
- Returns dict with:
  - `day`: Current day number
  - `hour`: Current hour (0-23)
  - `time_of_day`: Current period (morning/afternoon/evening/night)
  - `action_points`: Current action points
  - `max_action_points`: Maximum action points per day

**get_time_of_day() -> TimeOfDay**
- Get the current time of day period as an enum

## Usage Examples

### Example 1: Basic Usage
```python
from src.time_system import TimeSystem

# Initialize the system
game_time = TimeSystem()

# Check current status
status = game_time.get_status()
print(f"Day {status['day']}, {status['hour']}:00")

# Wait for 3 hours
result = game_time.wait(3)
print(result['message'])
```

### Example 2: Waiting Until a Specific Time
```python
# Wait until evening (8 PM)
result = game_time.wait_until(20)
if result['success']:
    print(f"Waited {result['hours_waited']} hours")
```

### Example 3: Managing Action Points
```python
# Spend action points on activities
if game_time.spend_action_point():
    print("Performed an action")
else:
    print("No action points remaining")

# Wait until next day to reset points
game_time.wait_until(8)  # Wait until 8 AM next day
```

### Example 4: Time of Day Detection
```python
time_period = game_time.get_time_of_day()
if time_period == TimeOfDay.NIGHT:
    print("It's nighttime - certain actions may be unavailable")
```

## Game Design Notes

The wait system is designed to support:
1. **Daily cycles** - Activities and events that occur at specific times
2. **Resource management** - Action points limit daily activities
3. **Strategic timing** - Players can wait to reach optimal times for actions
4. **Narrative pacing** - Time progression affects story and character interactions

## Testing

Run the test suite:
```bash
python -m unittest tests/test_time_system.py -v
```

Run the demo:
```bash
python examples/wait_demo.py
```

## Integration with Other Systems

The wait system is designed to integrate with:
- **Freedom Meter System** - Time affects freedom level
- **Detection System** - Time of day affects visibility and detection
- **Trust System** - Relationships may change over time
- **Mental Resilience** - Rest and time passage affect psychological state

---

**Author**: Chase Allen Ringquist  
**Version**: 0.1.0  
**License**: Proprietary - All Rights Reserved
