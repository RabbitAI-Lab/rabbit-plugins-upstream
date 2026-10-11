## Description:

Helps users plan, route, install, update, inventory, and distribute YottaMeta agent skills across local agent hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose suitable YottaMeta skills, inspect local installations, and manage installations and links across supported agent hosts with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation, linking, and removal operations can alter local skill directories.

Mitigation: Trust the publisher before granting filesystem access, review dry-run output, and confirm changes before execution.

Risk: Skipping package scanning may allow unverified skills to be installed.

Mitigation: Keep the scan gate enabled; avoid --skip-scan unless deliberately accepting unverified packages, and prefer host-native installs or exact-version commands in sensitive environments.

## Reference(s):

- [Project homepage (artifact metadata)](https://github.com/YottaMeta/yotta-skills)
- [Hub operations](artifact/references/hub.md)
- [Skill orchestration](artifact/references/orchestration.md)
- [Installation flow](artifact/references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Text and Markdown with shell commands; optional JSON for inventory and routing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report local skill inventory, suggested skill combinations, install status, and update checks.]

## Skill Version(s):

0.30.0 (source: server release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
