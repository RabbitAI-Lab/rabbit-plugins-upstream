## Description: <br>
Allows agents to log, list, search, and manage developer journal entries for projects using dev-log-cli in a structured SQLite database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to keep local project journals, recording progress, blockers, statuses, and searchable context through dev-log-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup script may install Python tooling and dev-log-cli into the user's environment. <br>
Mitigation: Install only when the dev-log-cli package source is trusted and review setup behavior before running it. <br>
Risk: Journal entries persist as project memory and may retain sensitive information. <br>
Mitigation: Avoid logging secrets, credentials, customer data, incident details, or sensitive internal reasoning, and periodically review or delete entries that should not be reused. <br>


## Reference(s): <br>
- [DevLog Agent Skill on ClawHub](https://clawhub.ai/crimsondevil333333/skills/devlog-agent-skill) <br>
- [dev-log-cli on PyPI](https://pypi.org/project/dev-log-cli/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate on local dev-log-cli project journal entries stored in SQLite.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
