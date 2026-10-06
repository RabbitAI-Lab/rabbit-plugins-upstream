## Description:

Helps agents plan skill combinations, recommend routes, install and update YottaMeta skills, inventory local skills, and manage a local skill hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can identify suitable skills, preview and manage YottaMeta skill installations, and inventory or distribute skills across local agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or updates can download packages and change skills across multiple agent directories.

Mitigation: Trust the package source, pin the npm version or use managed installation, and preview changes with dry-run before approving them.

Risk: Hub linking, removal, and automatic updates can alter local skill layouts.

Mitigation: Review each Hub link or remove operation and update --auto action before approval; avoid --skip-scan except in emergencies.

## Reference(s):

- [Project homepage (skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report skill routes, installation previews, inventory, and update status.]

## Skill Version(s):

0.29.5 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
