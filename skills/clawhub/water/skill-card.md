## Description: <br>
Tracks daily water intake from casual mentions and sets hydration targets from weight, exercise, heat, and health context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People use this skill to turn casual drink mentions into hydration logs and to get context-aware water, electrolyte, and safety guidance for everyday routines, exercise, heat, travel, illness, and relevant health conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently save health-related hydration details from broad casual mentions. <br>
Mitigation: Review before installing if those details should not be saved locally, and make sure the user can inspect and delete ~/Clawic/data/water/. <br>
Risk: Hydration guidance may touch illness, medications, fluid restriction, or symptoms that need clinical judgment. <br>
Mitigation: Use the skill's red-flag and condition rules to stop formula-based advice and route the user to a clinician when those cases appear. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/water) <br>
- [Clawic Water Tracker](https://clawic.com/skills/water) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Conversational text plus Markdown log and memory entries and YAML configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local hydration log, memory, and configuration files under ~/Clawic/data/water/.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
