## Description: <br>
Daily mood / energy / soreness / sleep capture primitive. Other lifekit skills read this to make state-aware suggestions instead of generic templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dsdevq](https://clawhub.ai/user/dsdevq) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to capture daily wellness state from natural-language check-ins and store it through the life-state CLI so other lifekit skills can make state-aware suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mood, energy, soreness, sleep quality, and notes are saved locally in plain JSON and may be read by other lifekit skills or local tools. <br>
Mitigation: Avoid sensitive medical details in notes unless local storage and backups are protected; use LIFE_STATE_DIR to place files in an appropriate location. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dsdevq/skills/life-state) <br>
- [lifekit personal-AI memory framework](https://github.com/dsdevq/lifekit) <br>
- [life-state repository link from README](https://github.com/dsdevq/life-state.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and terse text confirmations; the CLI returns YAML for state reads and summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the life-state binary and optionally LIFE_STATE_DIR to choose the local JSON store location.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
