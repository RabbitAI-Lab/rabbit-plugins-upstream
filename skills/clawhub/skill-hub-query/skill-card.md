## Description: <br>
Query, install, update, and edit AI agent skills on compatible Skill Hubs, including self-hosted hubs that implement the documented API contract. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to search hub catalogs, inspect skill versions, install or update skills, diagnose hub configuration, and edit owned skill card metadata when the target hub supports editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports a local file-handling flaw in edit-backup cleanup that deserves review before installation, especially for users who plan to use card editing. <br>
Mitigation: Review the skill before installing, use ordinary slug formats, require explicit confirmation before installs or card edits, and prefer a dedicated credentials file with restrictive permissions for long-lived tokens. <br>


## Reference(s): <br>
- [Skill Hub Query on ClawHub](https://clawhub.ai/songhonglei/skills/skill-hub-query) <br>
- [Skill Hub API Reference](references/api.md) <br>
- [skillhub.cn](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and user-readable tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local shell scripts that call compatible Hub APIs and read or write local cache, credentials, backups, and installed skill files.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence, SKILL.md, and changelog released 2026-07-17) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
