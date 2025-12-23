# Game Design Document: Isaac Bane Chase

## Core Design Philosophy

**Freedom through Choice**: Every player decision should meaningfully impact Isaac's journey toward freedom. The game respects player agency while telling a compelling story about reclaiming autonomy.

## Game Mechanics

### 1. Freedom Meter (Core Mechanic)

**Purpose**: Tracks Isaac's progress toward liberation

**Implementation**:
- Scale: 0-100
- Starting value: 10 (minimal freedom)
- Visible to player as a UI element
- Affected by actions, discoveries, and relationships

**Progression Triggers**:
- +5: Successful stealth action
- +10: Discovering important evidence
- +15: Gaining an ally's trust
- +20: Accessing restricted areas
- +25: Major story breakthroughs
- -10: Getting caught
- -15: Failed escape attempts

**Thresholds**:
- 0-25: Monitored (severe restrictions)
- 26-50: Aware (recognizing options)
- 51-75: Resistant (actively pursuing freedom)
- 76-100: Liberated (ready to escape)

### 2. Trust System

**Characters with Trust Levels**:
Each NPC has a trust rating (0-100) that affects their behavior:

- **Dr. Sarah Chen**: Medical staff, potential ally
- **Marcus Williams**: Fellow prisoner, mentor
- **Nurse Patterson**: Sympathetic but fearful
- **Guard Reynolds**: Conflicted about his job

**Trust Actions**:
- Honest dialogue: +10 trust
- Keeping promises: +15 trust
- Sharing information: +10 trust
- Being caught in a lie: -25 trust
- Betraying confidence: -50 trust

**Trust Benefits**:
- 25+: Basic assistance
- 50+: Valuable information
- 75+: Active support in escape
- 90+: Personal sacrifice for Isaac

### 3. Resource Management

**Resource Types**:

1. **Information**
   - Patient files
   - Security schedules
   - Facility layouts
   - Evidence of crimes

2. **Physical Items**
   - Key cards
   - Medical supplies
   - Communication devices
   - Tools for escape

3. **Time**
   - Limited actions per day
   - Certain activities only available at specific times
   - Urgency increases as story progresses

**Inventory System**:
- Limited carrying capacity (5 items)
- Items can be hidden in room
- Some items can be combined
- Strategic decisions about what to carry

### 4. Stealth and Detection

**Detection Mechanics**:
- **Alert Level**: Rises when Isaac acts suspiciously
- **Cool Down**: Alert level decreases over time
- **Consequences**: High alert triggers lockdowns

**Stealth Actions**:
- Observing guard patterns
- Moving during shift changes
- Using distractions
- Staying in allowed areas during monitored times

**Detection States**:
1. **Unaware** (0-25): Normal facility operations
2. **Suspicious** (26-50): Increased monitoring
3. **Alert** (51-75): Active searching
4. **Lockdown** (76-100): All movement restricted

### 5. Dialogue System

**Choice Types**:

1. **Information Gathering**
   - Ask questions
   - Observe reactions
   - Build relationships

2. **Persuasion**
   - Appeal to emotion
   - Use logic
   - Reference evidence

3. **Deception**
   - Misdirection
   - Feigning compliance
   - Strategic lies

**Dialogue Impact**:
- Affects trust levels
- Reveals/hides information
- Changes NPC behavior
- Influences freedom meter

### 6. Time and Day Cycle

**Daily Structure**:
- Morning: Breakfast, therapy sessions
- Afternoon: Recreation, work assignments
- Evening: Dinner, free time
- Night: Lights out, stealth opportunities

**Actions Per Day**: 4-6 meaningful actions
**Rest Requirement**: Isaac must rest to maintain health

### 7. Mental State

**Resilience System**:
- Represents Isaac's psychological strength
- Decreases with stress and setbacks
- Restored through rest and positive interactions
- Affects dialogue options and action effectiveness

**Low Resilience Effects**:
- Fewer dialogue options
- Reduced stealth effectiveness
- Impaired decision-making in cutscenes

## Puzzle Design

### Environmental Puzzles
1. **Security System Bypass**: Learn patterns, obtain codes
2. **Escape Route Planning**: Gather map pieces, study layouts
3. **Evidence Collection**: Connect disparate clues

### Social Puzzles
1. **Building Alliances**: Navigate complex relationships
2. **Information Trading**: Exchange knowledge strategically
3. **Manipulation**: Use knowledge of NPC motivations

### Logic Puzzles
1. **Schedule Optimization**: Plan actions around facility routines
2. **Resource Allocation**: Decide what to keep/use/trade
3. **Risk Assessment**: Evaluate costs and benefits

## Win Conditions

**Primary Goal**: Achieve freedom (escape the facility)

**Secondary Goals** (affect ending quality):
- Expose the truth (gather complete evidence)
- Save allies (help other prisoners)
- Minimize casualties (avoid violence)
- Preserve mental health (maintain resilience)

## Failure States

**Non-Fatal Failures**:
- Caught during stealth (reset position, -freedom)
- Failed persuasion (missed opportunity)
- Lost item (confiscated by staff)

**Critical Failures** (game over):
- Total mental breakdown (resilience = 0)
- Permanent lockdown (detection = 100 for extended period)
- Lethal confrontation (specific bad choices)

**Failure Recovery**: Most failures are learning opportunities, not game overs

## User Interface

**HUD Elements**:
1. Freedom Meter (top right)
2. Current objective (top left)
3. Time of day (top center)
4. Inventory quick-access (bottom right)
5. Mental state indicator (bottom left)

**Minimalist Design**: UI fades during dialogue/cutscenes

## Accessibility Features

- Skip dialogue option
- Adjustable text speed
- Multiple save slots
- Hint system (optional)
- Difficulty settings (affect detection sensitivity)

## Replayability

**Multiple Playthroughs Encouraged**:
- 5 distinct endings
- Different ally combinations
- Varied escape routes
- Achievement system tracking different approaches

**New Game+**: 
- Start with knowledge of facility layout
- Unlock special dialogue options
- Access to "true ending" path

## Technical Specifications (AGS)

- Resolution: 320x200 (classic) or 640x480 (enhanced)
- Color depth: 32-bit
- Audio: MP3/OGG for music, WAV for effects
- Script modules: Custom freedom system, trust system, inventory management
- Estimated playtime: 3-5 hours per playthrough

## Development Priorities

1. Core freedom and trust systems
2. Essential story path (main ending)
3. Stealth and detection mechanics
4. Dialogue system implementation
5. Additional endings and branches
6. Polish and playtesting

## Design Pillars

1. **Meaningful Choice**: Every decision matters
2. **Respect Player Agency**: Multiple valid approaches
3. **Thematic Consistency**: All mechanics reinforce freedom theme
4. **Emotional Engagement**: Characters feel real and compelling
5. **Strategic Depth**: Planning and thinking rewarded
