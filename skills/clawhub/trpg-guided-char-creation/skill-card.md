## Description: <br>
Use this skill when adding or updating guided character creation steps in a briefing_package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content maintainers use this skill to decide whether a TRPG briefing package should use standard form-based character creation, guided multi-step character creation, or both. It guides updates to config.yaml character_creation settings and related rules or data files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proposed config.yaml or related rules/data edits could misrepresent a specific TRPG system's character-creation rules. <br>
Mitigation: Review proposed edits against the game system before accepting them, especially character_creation steps, point budgets, max_initial values, and referenced options. <br>
Risk: Guided character-creation steps may reference races, classes, backgrounds, or other options that are missing from data/ or rules_sections/. <br>
Mitigation: Verify that every guided step has supporting option data available before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code, markdown] <br>
**Output Format:** [Markdown guidance with YAML configuration examples and file-editing recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces human-reviewable recommendations and proposed edits for TRPG briefing package character-creation configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
