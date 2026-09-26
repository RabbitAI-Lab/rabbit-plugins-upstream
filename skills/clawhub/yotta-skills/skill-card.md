## Description:

Plans and routes YottaMeta skill combinations, inventories installed skills, and provides commands to install or update the skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose YottaMeta skill combinations, check installed skills, and preview or run family installations and updates with their approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating the family downloads packages and changes agent skill directories.

Mitigation: Review the planned targets, use --dry-run first, and prefer a pinned package version before approving installation.

Risk: Global installation can affect multiple known agent directories.

Mitigation: Avoid install.sh -g/--global unless you intend to change all supported agent directories.

Risk: Enabling optional MCP integration or global memory can change agent configuration and future behavior.

Mitigation: Review the proposed configuration and target files, and require explicit approval before allowing writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing suggestions include candidate skills, order, confidence, and installation status; installation requires user approval.]

## Skill Version(s):

0.19.23 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
