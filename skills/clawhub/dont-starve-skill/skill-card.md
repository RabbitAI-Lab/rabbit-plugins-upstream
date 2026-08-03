## Description: <br>
Guide for Don't Starve / DST survival, character selection, boss fights, recipes, base building, multiplayer strategy, and lore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morandot](https://clawhub.ai/user/morandot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External players use this skill to get actionable Don't Starve, Don't Starve Together, Shipwrecked, and Hamlet guidance for character choice, seasonal planning, recipes, base building, boss fights, multiplayer coordination, and lore. When local file access is available, the skill can tailor guidance from a structured local survivor profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain local gameplay facts such as game version, progress, preferred characters, and preferences. <br>
Mitigation: Install only if local profile retention is acceptable; set DONTSTARVE_MEMORY_DIR to an isolated directory or review and remove ~/.config/dont-starve-skill/survivor-profile.json when retention is not wanted. <br>
Risk: Current-version, patch, and mod compatibility guidance can become outdated. <br>
Mitigation: For latest-update or mod-compatibility questions, browse when internet access is available or clearly state when guidance is based on non-current knowledge. <br>


## Reference(s): <br>
- [Answer Templates](references/answer-templates.md) <br>
- [Style Examples](references/examples.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/morandot/skills/dont-starve-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with occasional shell command and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read or update a local survivor-profile JSON file when local file access is available.] <br>

## Skill Version(s): <br>
0.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
