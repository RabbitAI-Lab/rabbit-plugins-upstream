## Description: <br>
Agent Skill for Don't Starve / DST survival guides covering character selection, seasonal preparation, boss strategy, base building, Crock Pot recipes, survival pacing, DST multiplayer coordination, Shipwrecked and Hamlet DLC mechanics, mod recommendations, terminology, lore, and local survivor-profile-aware guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morandot](https://clawhub.ai/user/morandot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to receive concise, actionable gameplay guidance for Don't Starve, Don't Starve Together, Shipwrecked, and Hamlet. It helps an agent tailor survival planning, boss preparation, recipes, base building, multiplayer roles, terminology, lore, and mod advice to the user's stated mode and local survivor profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create and maintain a local gameplay profile containing stated preferences, progress, characters, and world settings. <br>
Mitigation: Review or delete ~/.config/dont-starve-skill/survivor-profile.json, or set DONTSTARVE_MEMORY_DIR to control where that data is stored. <br>
Risk: Gameplay guidance may be incorrect for a user's current Don't Starve mode, DLC, mod set, or recent patch. <br>
Mitigation: Separate DS, DST, Shipwrecked, and Hamlet guidance, ask for missing mode details when needed, and browse for current-version or mod-compatibility questions when internet access is available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/morandot/skills/dont-starve-skill) <br>
- [Server-resolved GitHub source path](https://github.com/morandot/dont-starve-skill/tree/main/dont-starve-skill) <br>
- [Project homepage](https://github.com/morandot/dont-starve-skill) <br>
- [Answer templates](references/answer-templates.md) <br>
- [Style examples](references/examples.md) <br>
- [Local survivor profile script](scripts/memory.py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with occasional inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update a local survivor profile when file access is available.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
