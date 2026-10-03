## Description:

Helps agent users plan and route YottaMeta skill combinations, inspect installed skills, and preview or manage family-wide installations and updates across local agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to select YottaMeta skills for a task, inspect local installations, and, after reviewing a preview, install, update, link, or roll back skills across agent directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing, updating, linking, or rolling back skills can change multiple local agent directories.

Mitigation: Preview changes with dry-run first and confirm the target directories and skill versions before proceeding.

Risk: Bypassing the installation scan can allow unverified skills to be installed.

Mitigation: Keep scanning enabled unless you deliberately accept the risk of an unverified installation.

Risk: Optional setup may change agent instructions or MCP server configuration.

Mitigation: Review proposed AGENTS.md, CLAUDE.md, and mcpServers edits before approving them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage listed in skill metadata](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration instructions]

**Output Format:** [Text or JSON with skill recommendations, inventory results, and installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation and update operations can modify local skill directories; recommendations alone do not install skills.]

## Skill Version(s):

0.28.2 (source: release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
