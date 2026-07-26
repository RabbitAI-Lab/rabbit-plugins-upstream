## Description: <br>
Organized research and knowledge management for agents, supporting note capture, topic lists, cross-note search, and markdown export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to keep structured research notes across sessions, search prior findings, and export completed topic notes to markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research notes persist across sessions and may contain sensitive information if users store secrets or private instructions. <br>
Mitigation: Avoid storing passwords, API keys, private keys, or highly sensitive instructions in research notes. <br>
Risk: Markdown export writes files to user-selected paths. <br>
Mitigation: Review export paths before running the export command; version 1.0.1 restricts exports to safe directories and blocks system paths and sensitive dotfiles. <br>


## Reference(s): <br>
- [Research Assistant on ClawHub](https://clawhub.ai/johstracke/skills/research-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown and terminal text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores notes in a local JSON database and can export topic notes as markdown.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
