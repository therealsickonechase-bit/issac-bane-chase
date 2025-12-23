# Freedom Mechanics: Technical Specification

## Overview

This document details the technical implementation of the "Freedom" concept in Isaac Bane Chase. Freedom is not just a theme but a quantifiable game system that drives gameplay and narrative.

---

## 1. Freedom Meter System

### Core Variable
```
int freedomScore = 10;  // Range: 0-100, starts at 10
```

### Freedom States

#### State 1: Monitored (0-25)
- **Description**: Isaac is under heavy surveillance
- **Gameplay Impact**:
  - Limited movement options
  - Restricted dialogue choices
  - Higher detection sensitivity
  - Cannot access restricted areas
  - Guard patrols more frequent

#### State 2: Aware (26-50)
- **Description**: Isaac understands his situation
- **Gameplay Impact**:
  - More dialogue options available
  - Can gather information more freely
  - Slightly reduced detection sensitivity
  - Some restricted areas become accessible
  - Can build initial trust with NPCs

#### State 3: Resistant (51-75)
- **Description**: Isaac actively working toward freedom
- **Gameplay Impact**:
  - All dialogue trees available
  - Can plan and execute escape strategies
  - Moderate detection sensitivity
  - Most areas accessible with planning
  - NPCs respond to leadership
  - Can recruit allies

#### State 4: Liberated (76-100)
- **Description**: Isaac is ready for escape
- **Gameplay Impact**:
  - Maximum player agency
  - Can execute final escape plan
  - Lowest detection sensitivity (experienced at stealth)
  - All gameplay systems fully unlocked
  - Endings become available

### Freedom Score Modifications

#### Positive Actions
```
// Discovery and Knowledge
+5  : Find evidence document
+10 : Discover security weakness
+15 : Recover a memory
+20 : Access restricted area first time
+25 : Major story revelation

// Social Interactions
+5  : Honest conversation
+10 : Gain NPC trust threshold
+15 : Convert guard/staff to ally
+20 : Form alliance with Marcus

// Stealth and Action
+5  : Successful stealth action
+10 : Acquire key item without detection
+15 : Disable security measure
+20 : Complete room puzzle

// Mental Freedom
+5  : Resist manipulation
+10 : Assert autonomy in dialogue
+15 : Refuse medication (risky)
+20 : Confront authority figure
```

#### Negative Actions
```
// Detection and Failure
-5  : Minor suspicious action noticed
-10 : Caught in restricted area
-15 : Failed stealth attempt
-20 : Failed escape attempt
-25 : Betrayed by trusted NPC

// Compliance and Submission
-5  : Accept obvious lie
-10 : Full compliance with unjust order
-15 : Betray another patient
-20 : Give up information under pressure

// Mental/Physical State
-5  : Accept unneeded medication
-10 : Mental resilience critically low
-15 : Prolonged isolation
```

### Freedom Meter Display

**Visual Representation**:
- UI element: Progress bar with icon
- Position: Top right of screen
- Color scheme:
  - 0-25: Red (Danger)
  - 26-50: Orange (Caution)
  - 51-75: Yellow (Progress)
  - 76-100: Green (Liberation)
- Animated: Pulses when changed
- Tooltip: Shows exact number and current state

**Narrative Feedback**:
When freedom score changes significantly, Isaac's internal monologue reflects it:
- "I'm starting to see a way out..."
- "They're watching me more closely now."
- "I can feel my resolve strengthening."
- "I'm ready. Time to take control."

---

## 2. Trust System

### NPC Trust Values

Each major NPC has a trust variable:
```
int trustSarahChen = 30;      // Starts cautiously positive
int trustMarcusWilliams = 20;  // Starts neutral
int trustEmilyPatterson = 40;  // Starts sympathetic
int trustReynolds = 10;        // Starts low/professional
int trustColdwell = 0;         // Antagonist (cannot trust)
int trustRivera = 25;          // Starts ambiguous
```

### Trust Thresholds and Effects

#### Dr. Sarah Chen
```
0-24:   Hostile - Reports Isaac's behavior
25-49:  Professional - Neutral, by-the-book
50-74:  Concerned - Begins questioning facility
75-89:  Allied - Provides information and small help
90-100: Committed - Actively assists escape, risks career
```

**Trust-Locked Actions**:
- 50+: Reveals doubts about facility
- 60+: Shares patient file information
- 75+: Provides key card temporarily
- 90+: Creates diversion during escape

#### Marcus Williams
```
0-24:   Suspicious - Won't share information
25-49:  Observing - Tests Isaac's character
50-74:  Respectful - Begins mentoring
75-89:  Allied - Shares escape plans
90-100: Brother-in-arms - Coordinates escape together
```

**Trust-Locked Actions**:
- 40+: Teaches stealth basics
- 60+: Reveals security knowledge
- 75+: Shares his escape plan
- 90+: Willing to risk his escape to help Isaac

#### Nurse Emily Patterson
```
0-24:   Scared - Avoids Isaac
25-49:  Guilty - Minimal interaction
50-74:  Sympathetic - Small kindnesses
75-89:  Helpful - Provides minor assistance
90-100: Courageous - Takes significant risk to help
```

**Trust-Locked Actions**:
- 50+: "Forgets" to lock a door
- 65+: Reduces medication dosage
- 80+: Provides information about shift changes
- 95+: Helps with distraction

### Trust Modification Events

**Building Trust**:
```
+5  : Share personal information
+10 : Keep a promise
+10 : Show vulnerability
+15 : Defend NPC to others
+15 : Risk something to help them
+20 : Save them from consequence
```

**Losing Trust**:
```
-10 : Minor lie discovered
-15 : Break a promise
-20 : Betray confidence
-25 : Manipulate them harmfully
-50 : Major betrayal
```

### Trust and Freedom Interaction

Trust and Freedom are interconnected:
- High trust with allies → More freedom opportunities
- High freedom score → NPCs more likely to trust Isaac
- Low freedom + high trust → NPCs motivated to help
- High freedom + low trust → Isaac must proceed alone

---

## 3. Detection System

### Alert Level
```
int alertLevel = 0;  // Range: 0-100
```

### Detection States

#### Green (0-25): Normal Operations
- Guards follow routine patrols
- Staff interact normally
- All standard areas accessible
- Cameras on regular rotation

#### Yellow (26-50): Increased Vigilance
- Guards check restricted areas more often
- Staff ask more questions
- Some areas temporarily locked down
- Cameras scan more frequently

#### Orange (51-75): Active Search
- Guards actively looking for Isaac
- Limited movement allowed
- Most restricted areas locked
- Cannot perform stealth actions safely

#### Red (76-100): Facility Lockdown
- All guards on high alert
- Isaac confined to room
- All restricted areas sealed
- Escape attempt extremely difficult

### Alert Level Changes

**Increases**:
```
+10 : Seen in off-limits area
+15 : Acting suspiciously
+20 : Caught with contraband
+25 : Failed stealth action
+30 : Setting off alarm
```

**Decreases** (over time):
```
-5 per time period : If Isaac behaves normally
-10 per time period : If Isaac in his room during lockdown
-15 per time period : If Isaac cooperates with increased security
```

**Instant Resets**:
- Major story event that shifts attention
- Facility-wide emergency (not Isaac-related)
- Successful frame job (advanced tactic)

### Detection Mechanics

**Line of Sight**:
- Guards and cameras have vision cones
- Breaking line of sight before full detection = safe
- Player feedback: UI warning when entering detection zone

**Sound**:
- Running creates noise
- Knocking over objects creates noise
- Noise attracts attention but not instant detection

**Suspicious Behavior**:
- Being in wrong area at wrong time
- Carrying obvious contraband
- Acting nervous (low resilience)

---

## 4. Time Management System

### Time Structure
```
enum TimeOfDay {
    MORNING,      // 6 AM - 12 PM
    AFTERNOON,    // 12 PM - 6 PM
    EVENING,      // 6 PM - 10 PM
    NIGHT         // 10 PM - 6 AM
}

int currentDay = 1;
TimeOfDay currentTime = MORNING;
int actionsRemaining = 4;  // Resets each time period
```

### Daily Schedule

#### Morning (6 AM - 12 PM)
- Breakfast: 7 AM
- Therapy sessions: 9 AM - 11 AM
- Free time: 11 AM - 12 PM
- **Available Actions**: 4
- **Opportunities**: Talk to Dr. Chen, explore common areas

#### Afternoon (12 PM - 6 PM)
- Lunch: 12 PM
- Recreation: 1 PM - 3 PM
- Work assignments: 3 PM - 5 PM
- **Available Actions**: 4
- **Opportunities**: Social interactions, recreational area access

#### Evening (6 PM - 10 PM)
- Dinner: 6 PM
- Free time: 7 PM - 9 PM
- Prepare for bed: 9 PM
- **Available Actions**: 3
- **Opportunities**: Private conversations, gather items

#### Night (10 PM - 6 AM)
- Lights out: 10 PM
- Guard shift change: 2 AM
- Wake up: 6 AM
- **Available Actions**: 2 (risky)
- **Opportunities**: Stealth, restricted areas, less supervision

### Action Types

**Free Actions** (don't consume action points):
- Movement within allowed areas
- Basic dialogue
- Examining objects
- Reading inventory items

**Standard Actions** (consume 1 action point):
- Important conversations
- Searching containers
- Simple puzzles
- Using items

**Major Actions** (consume 2 action points):
- Complex puzzles
- Stealth infiltration
- Important story events
- Risky actions

### Time Pressure

As the story progresses, time becomes more critical:
- Days 1-3: Learning phase, no pressure
- Days 4-7: Growing urgency
- Days 8-10: High pressure, authorities closing in
- Day 10+: Critical - must escape or face consequences

---

## 5. Resource Management

### Inventory System
```
int inventoryCapacity = 5;
bool[] hiddenStash = new bool[10];  // Items hidden in room
```

### Resource Types

#### Information (No inventory space)
```
bool[] discoveredDocuments = new bool[20];
bool[] learnedSecrets = new bool[15];
bool[] mappedAreas = new bool[10];
```

#### Physical Items (Uses inventory)
```
Item[] inventory = new Item[5];

struct Item {
    string name;
    string description;
    ItemType type;
    bool canCombine;
    int[] combinesWith;
}

enum ItemType {
    KEY_CARD,
    TOOL,
    EVIDENCE,
    CONSUMABLE,
    QUEST_ITEM
}
```

#### Key Items
- **Level 1 Key Card**: Common areas
- **Level 2 Key Card**: Staff areas
- **Level 3 Key Card**: Restricted areas
- **Makeshift lockpick**: One-time use, medium difficulty locks
- **Guard uniform**: Disguise (limited use)
- **Smartphone**: Evidence collection, communication
- **Medication**: Can be stockpiled or refused
- **Flashlight**: Navigate dark areas
- **Rope**: Escape route component

### Resource Strategy

Players must decide:
- What to carry vs. what to hide
- When to use vs. when to save
- What to trade vs. what to keep
- Risk of being caught with contraband

---

## 6. Mental Resilience System

### Resilience Variable
```
int mentalResilience = 75;  // Range: 0-100
```

### Resilience Effects

#### High Resilience (75-100)
- All dialogue options available
- Maximum stealth effectiveness
- Clear thinking in cutscenes
- Resists manipulation

#### Medium Resilience (50-74)
- Most dialogue options available
- Standard stealth effectiveness
- Occasional self-doubt
- Can be manipulated sometimes

#### Low Resilience (25-49)
- Limited dialogue options
- Reduced stealth effectiveness
- Frequent self-doubt
- Vulnerable to manipulation

#### Critical Resilience (0-24)
- Very few dialogue options
- Poor stealth ability
- Questioning reality
- Highly vulnerable
- Risk of game over

### Resilience Changes

**Decreases**:
```
-5  : Minor setback
-10 : Failed escape attempt
-15 : Betrayal by ally
-20 : Prolonged isolation
-25 : Major traumatic event
```

**Increases**:
```
+5  : Good night's rest
+10 : Positive interaction
+15 : Small victory
+20 : Achieving major goal
+25 : Significant breakthrough
```

### Recovery Actions

- **Rest**: +10 resilience (requires time)
- **Meditation**: +5 resilience (requires quiet space)
- **Conversation**: +5-15 resilience (requires trusted NPC)
- **Progress**: +10-20 resilience (achieving objectives)

---

## 7. Integration and Balance

### System Interactions

**Freedom & Trust**:
```
// Global multipliers for system interactions
float trustMultiplier = 1.0;
float freedomGainMultiplier = 1.0;

// Check if high freedom score boosts trust building
if (freedomScore > 50) {
    // NPCs more willing to trust a confident Isaac
    trustMultiplier = 1.2;
}

// Calculate total trust across all NPCs
int totalTrust = trustSarahChen + trustMarcusWilliams + 
                 trustEmilyPatterson + trustReynolds + trustRivera;

if (totalTrust > 200) {  // Sum of all NPC trust
    // Strong ally network makes freedom easier to achieve
    freedomGainMultiplier = 1.15;
}
```

**Detection & Resilience**:
```
if (mentalResilience < 30) {
    // More easily detected (nervous behavior)
    detectionSensitivity *= 1.5;
}
```

**Time & Alert**:
```
if (currentTime == NIGHT && alertLevel < 50) {
    // Stealth bonus at night when alert is low
    stealthBonus = 20;
}
```

### Balance Considerations

**Freedom Progression Curve**:
- Days 1-2: Reach 25-30 freedom (Aware state)
- Days 3-5: Reach 50-60 freedom (Resistant state)
- Days 6-8: Reach 75-85 freedom (Liberated state)
- Days 9-10: Escape attempt

**Difficulty Tuning**:
- Easy: Higher freedom gains, lower detection
- Normal: Balanced as specified
- Hard: Lower freedom gains, higher detection, limited saves

### Win Condition Check
```
// Helper function to check if player has required items for escape
bool hasRequiredItems() {
    // At minimum, player needs either a key card or alternative escape tool
    bool hasAccessItem = (hasItem("Level3KeyCard") || 
                          hasItem("MasterKeyCard") || 
                          hasItem("GuardUniform"));
    
    // And evidence to accomplish complete freedom ending
    bool hasEvidence = discoveredDocuments.Count(true) >= 10;
    
    return hasAccessItem && hasEvidence;
}

// Main escape attempt check
bool canAttemptEscape() {
    return freedomScore >= 75 &&
           (trustSarahChen >= 75 || trustMarcusWilliams >= 75) &&
           hasRequiredItems() &&
           alertLevel < 50;
}
```

---

## 8. Saving Freedom Development State

All freedom-related variables must be saved:
```
SaveGame {
    // Core systems
    int freedomScore;
    int alertLevel;
    int mentalResilience;
    int currentDay;
    TimeOfDay currentTime;
    int actionsRemaining;
    
    // Trust values
    int[] npcTrust;
    
    // Resources
    Item[] inventory;
    bool[] hiddenStash;
    bool[] discoveredDocuments;
    
    // Story state
    int[] storyFlags;
    int[] completedObjectives;
}
```

---

## Conclusion

These freedom mechanics create a cohesive system where:
- Player choices meaningfully impact gameplay
- Multiple approaches are viable
- The theme of freedom is mechanically reinforced
- Systems interact to create emergent gameplay
- Progression feels earned and satisfying

The technical implementation supports the narrative goal: developing Isaac's freedom.
