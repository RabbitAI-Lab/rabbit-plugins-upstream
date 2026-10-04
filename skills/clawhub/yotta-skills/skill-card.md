## Description:

Helps agents plan and route YottaMeta skills, inventory local skills, and guide confirmed installation, updates, and distribution across agent hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to select YottaMeta skill combinations, review local inventories, and install or update skills across supported agent hosts with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and Hub commands can change local agent skills, including downloading, updating, linking, or removing them.

Mitigation: Review dry-run output before changes and prefer host-native OpenClaw install or update commands where available.

Risk: Skipping scans or using a floating installer version can expose installations to unreviewed changes.

Mitigation: Keep scanning enabled and pin the installer version in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](artifact/references/orchestration.md)
- [Installation guide](artifact/references/install-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include skill recommendations, installation previews, and inventory summaries.]

## Skill Version(s):

0.28.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
