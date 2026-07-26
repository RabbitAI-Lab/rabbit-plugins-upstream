## Description: <br>
A standardized journaling skill for OpenClaw agents to track progress, tasks, and project status using dev-log-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to keep structured project journals, record milestones and blockers, and retrieve recent project context through dev-log-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup installs the unpinned PyPI package dev-log-cli and may install pipx, creating normal third-party package supply-chain exposure. <br>
Mitigation: Review the package source and dependencies, pin a known package version when operating under stricter reproducibility requirements, or run setup in an isolated environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/crimson-devlog-agent) <br>
- [dev-log-cli on GitHub](https://github.com/CrimsonDevil333333/dev-log-cli) <br>
- [dev-log-cli on PyPI](https://pypi.org/project/dev-log-cli/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational guidance for installing and using dev-log-cli; setup may install pipx and dev-log-cli if missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
