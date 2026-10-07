## Description:

Helps agents plan and route YottaMeta skill combinations, inventory installed skills, and manage local skill installation, updates, and Hub links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose YottaMeta skill combinations, inspect local installations, and manage skill distribution across agent directories with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation, updates, and Hub links can change skills across local agent directories.

Mitigation: Review dry-run previews before changes and pin package versions for repeatable installations.

Risk: Optional provider, MCP, or global-memory settings can alter agent behavior.

Mitigation: Review the proposed configuration and approve it explicitly before enabling it.

## Reference(s):

- [Yotta Skills homepage](https://github.com/YottaMeta/yotta-skills)
- [Hub guide](references/hub.md)
- [Installation flow](references/install-flow.md)
- [Orchestration guide](references/orchestration.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown or CLI text; optional JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide routing suggestions, installed-skill inventories, and installation previews.]

## Skill Version(s):

0.29.6 (source: skill frontmatter, server release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
