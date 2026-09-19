## Description:

Baidu Maps enables agents to search and read Baidu Maps data, including places, geocoding, routes, districts, IP location, and weather, through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Baidu Maps lookups such as geocoding, place search, route planning, district search, IP location, and weather using a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include commands that execute remote installer scripts directly in a shell.

Mitigation: Install the oo CLI from a verified source or inspect and verify the installer before execution.

Risk: Using the connector sends Baidu Maps queries through OOMOL-connected infrastructure.

Mitigation: Share only location and query data appropriate for the connected OOMOL and Baidu Maps accounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-maps)
- [Baidu Maps homepage](https://lbsyun.baidu.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
