# GitHub Copilot Instructions – issac-bane-chase

## Project Overview

This is a narrative adventure game project focused on player agency and freedom mechanics. The project is a proprietary, copyrighted work by Chase Allen Ringquist, created for MIT academic peer review.

## Tech Stack

- **Primary Language**: Python
- **Game Engine**: Adventure Game Studio (AGS)
- **Project Type**: Narrative-driven adventure game with complex systems

## Licensing and Copyright

**CRITICAL**: This is proprietary software with ALL RIGHTS RESERVED.

- **Copyright**: © 2025 Chase Allen Ringquist
- **License**: Proprietary (NOT open source)
- **Author**: Chase Allen Ringquist (@therealsickonechase-bit)

### When generating or modifying code:

1. **NEVER** suggest or add open source licenses (MIT, Apache, GPL, etc.)
2. **ALWAYS** maintain copyright notices: `© 2025 Chase Allen Ringquist. All Rights Reserved.`
3. **NEVER** suggest making the project open source or publicly licensed
4. All code is proprietary and confidential

## Coding Guidelines

### Python Code Standards

- Follow PEP 8 style guide for Python code
- Use type hints where appropriate for better code clarity
- Prefer descriptive variable and function names
- Use docstrings for all classes and functions
- Keep functions focused and single-purpose

### Documentation Requirements

- Document all public APIs with clear docstrings
- Include type information in docstrings
- Explain complex algorithms or game mechanics inline
- Maintain clear separation between game systems

## Game Systems Architecture

This project includes several interconnected systems:

1. **Freedom Meter System**: 0-100 scale tracking with state machines
2. **Detection System**: Alert level mechanics with line-of-sight calculations
3. **Trust System**: Multi-NPC relationship management algorithms
4. **Time Management**: Action point system with daily cycle scheduling
5. **Resource Management**: Inventory and hidden stash mechanics
6. **Mental Resilience System**: Psychological state affecting gameplay
7. **Save/Load Architecture**: Complete game state serialization

### When working with game systems:

- Maintain consistency between interconnected systems
- Document state transitions and dependencies
- Consider edge cases in player interactions
- Preserve game balance and intended difficulty

## Security and IP Protection

- **NEVER** include real secrets, API keys, or credentials in code
- **ALWAYS** respect the proprietary nature of the codebase
- Do not suggest publishing sensitive game mechanics publicly
- Maintain confidentiality of unique algorithms and designs

## File Organization

Based on `.gitignore`, the following are build artifacts and should not be committed:

- `_Debug/`, `Compiled/` directories
- `AudioCache/` directory
- `*.exe` files
- `*.dmp` files
- Temporary files like `~aclzw.tmp`, `game28.dta`
- User settings: `*.user` files
- Log files: `warnings.log`

## Testing Approach

- Write tests for critical game systems
- Test state transitions thoroughly
- Validate edge cases in player interactions
- Ensure save/load functionality maintains integrity

## MIT Peer Review Context

This project is submitted for MIT academic peer review to:

- Validate technical quality and innovation
- Establish academic recognition
- Protect intellectual property
- Receive expert feedback on game design and implementation

When suggesting improvements, consider academic rigor and innovation.

## Contact

**Author**: Chase Allen Ringquist  
**GitHub**: @therealsickonechase-bit  
**Email**: therealsickone.chase@gmail.com

---

**Remember**: This is proprietary work. All suggestions and code must respect the copyright and licensing requirements.
