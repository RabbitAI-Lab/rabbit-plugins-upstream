## Description: <br>
A standardized journaling skill for OpenClaw agents to track progress, tasks, and project status using dev-log-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to keep structured developer logs for progress, blockers, project milestones, task status, search, and review through dev-log-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup script can install pipx and dev-log-cli from PyPI at the user level. <br>
Mitigation: Review the setup script and package source before installation, and install in an environment where user-level Python tooling changes are acceptable. <br>
Risk: Developer log entries may persist locally and could contain sensitive project, customer, credential, or incident details if entered by a user. <br>
Mitigation: Avoid recording secrets or sensitive data, and verify where dev-log-cli stores its SQLite database and how entries can be deleted or redacted. <br>


## Reference(s): <br>
- [Devlog Skill on ClawHub](https://clawhub.ai/crimsondevil333333/skills/devlog-skill) <br>
- [dev-log-cli on PyPI](https://pypi.org/project/dev-log-cli/) <br>
- [pipx installation guidance](https://github.com/pypa/pipx#install-pipx) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; devlog commands produce CLI text and local journal records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may create or update local devlog entries through dev-log-cli.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
