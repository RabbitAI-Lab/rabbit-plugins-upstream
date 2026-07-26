## Description: <br>
问道笔录 - 修仙文字冒险游戏。玩家从凡人开始修炼，经历炼气、筑基、金丹、元婴、化神、渡劫、飞升七大境界，通过选择塑造道心，最终成就修仙之路。支持转世传承、角色成长、物品系统。适用于修仙题材、角色扮演、文字冒险等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ouwenjie03](https://clawhub.ai/user/ouwenjie03) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Players use this skill to run a Chinese cultivation-themed text adventure where choices guide character growth, inventory, biography, reincarnation, and progression across seven realms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update game_state.md as a local save file, which may overwrite or change prior game progress. <br>
Mitigation: Install it in a dedicated folder and keep a backup of game_state.md when preserving an existing run matters. <br>
Risk: Inventory choices can discard items when the player's instruction is unclear. <br>
Mitigation: Use explicit accept, decline, keep, and discard instructions when managing inventory items. <br>


## Reference(s): <br>
- [Game Start and Initialization](references/ch00_start.md) <br>
- [Qi Refining Realm Journey](references/ch01_qi_refining.md) <br>
- [Foundation Establishment Realm](references/ch02_foundation.md) <br>
- [Golden Core Realm](references/ch03_golden_core.md) <br>
- [Nascent Soul Realm](references/ch04_nascent_soul.md) <br>
- [Spirit Transformation Realm](references/ch05_spirit_transformation.md) <br>
- [Tribulation Realm](references/ch06_tribulation.md) <br>
- [Ascension and Reincarnation](references/ch07_ascension.md) <br>
- [Managing Biography System](references/system_biography_system.md) <br>
- [Managing Character System](references/system_character_system.md) <br>
- [Managing Inventory System](references/system_inventory_system.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown narrative with local game_state.md save-file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates game_state.md during play; no hidden execution, credential access, or data exfiltration was found in the security scan.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-01-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
