## Description: <br>
A Chinese-language interactive horror mystery role-playing game where an agent guides players through a snowbound hotel investigation with branching story paths, clue discovery, character interaction, and multiple endings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ouwenjie03](https://clawhub.ai/user/ouwenjie03) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to run a Chinese-language interactive horror mystery text adventure. The agent narrates scenes, responds to natural-language player choices, tracks clues and character state, and guides the story toward multiple possible endings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gameplay state may be stored in a local game_state.json file, including choices, progress, player notes, or names. <br>
Mitigation: Use non-sensitive player names and notes, and review local game-state files before sharing logs or artifacts. <br>
Risk: The adventure includes horror, violence, and psychological thriller content. <br>
Mitigation: Use with age-appropriate audiences and present the content warning before gameplay. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/ouwenjie03/skills/banshee-s-last-cry) <br>
- [Game overview](artifact/SKILL.md) <br>
- [Chapter 00: Start](artifact/references/ch00_start.md) <br>
- [Chapter 1A: Investigation](artifact/references/ch1a_investigate.md) <br>
- [Chapter 1B: Ambush](artifact/references/ch1b_ambush.md) <br>
- [Chapter 1C: Solo Route](artifact/references/ch1c_solo.md) <br>
- [Chapter 2A: Chase](artifact/references/ch2a_chase.md) <br>
- [Chapter 2B: Suspect Confrontation](artifact/references/ch2b_suspect.md) <br>
- [Chapter 2C: Attack](artifact/references/ch2c_attack.md) <br>
- [Chapter 2D: Trap](artifact/references/ch2d_trap.md) <br>
- [Chapter 2E: Alone](artifact/references/ch2e_alone.md) <br>
- [Chapter 3A: Basement](artifact/references/ch3a_basement.md) <br>
- [Chapter 3B: Second Death](artifact/references/ch3b_death2.md) <br>
- [Chapter 3C: Split](artifact/references/ch3c_split.md) <br>
- [Chapter 3D: Team](artifact/references/ch3d_team.md) <br>
- [Chapter 3E: Escape](artifact/references/ch3e_escape.md) <br>
- [Chapter 3F: Reveal](artifact/references/ch3f_reveal.md) <br>
- [Chapter 3G: Hero](artifact/references/ch3g_hero.md) <br>
- [Chapter 4: Endings](artifact/references/ch4_endings.md) <br>
- [Character information](artifact/references/system_character_info.md) <br>
- [Clue system](artifact/references/system_clue_system.md) <br>
- [Game state system](artifact/references/system_game_state.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Chinese-language Markdown narrative with JSON game-state updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Progressive narrative segments; may create or update local game_state.json with gameplay choices and progress.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
