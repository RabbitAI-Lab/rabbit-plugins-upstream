## Description: <br>
Whispers from the Star is a xianxia text adventure that guides players from mortal cultivation through seven realms using Dao Heart choices, reincarnation inheritance, character growth, and inventory management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ouwenjie03](https://clawhub.ai/user/ouwenjie03) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External players and agent users use this skill to run a choice-driven xianxia role-playing text adventure and maintain fictional character, biography, and inventory state across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and updates a local game_state.md save file for fictional game progress. <br>
Mitigation: Keep game_state.md limited to fictional game content and back it up before resets, reincarnation, or new-cycle transitions. <br>
Risk: Vague inventory discard choices may remove an in-game item. <br>
Mitigation: Give explicit item names or item numbers when discarding, transferring, or replacing inventory items. <br>


## Reference(s): <br>
- [Whispers from the Star on ClawHub](https://clawhub.ai/ouwenjie03/skills/whispers-from-the-star) <br>
- [Game Start and Initialization](references/ch00_start.md) <br>
- [Qi Refining Realm Journey](references/ch01_qi_refining.md) <br>
- [Foundation Establishment Realm](references/ch02_foundation.md) <br>
- [Golden Core Realm](references/ch03_golden_core.md) <br>
- [Nascent Soul Realm](references/ch04_nascent_soul.md) <br>
- [Spirit Transformation Realm](references/ch05_spirit_transformation.md) <br>
- [Tribulation Realm](references/ch06_tribulation.md) <br>
- [Ascension and Reincarnation](references/ch07_ascension.md) <br>
- [Managing Character System](references/system_character_system.md) <br>
- [Managing Inventory System](references/system_inventory_system.md) <br>
- [Managing Biography System](references/system_biography_system.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown narrative and structured save-state updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update a local fictional game_state.md save file when the user plays through the adventure.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
