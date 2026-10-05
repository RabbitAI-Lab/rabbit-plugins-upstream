## Description:

Helps agents plan YottaMeta skill combinations, recommend routes, inventory installed skills, and manage installations across local agent hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose complementary YottaMeta skills, review suggested installation commands, and manage local skill inventories and distribution across agent hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or linking may change local skill directories across multiple agent hosts.

Mitigation: Review target directories and preview installs, links, and removals with --dry-run before confirming changes.

Risk: Downloaded skill packages and update choices can affect the local agent environment.

Mitigation: Prefer pinned versions or OpenClaw-managed installation when applicable, and review the installation plan.

Risk: Optional MCP, provider, and memory features can write local configuration or usage files.

Mitigation: Enable these features only after reviewing the files they write and approving the change.

## Reference(s):

- [Project homepage (ClawHub metadata)](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](references/orchestration.md)
- [Hub management guide](references/hub.md)
- [Installation flow](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Text or Markdown guidance, shell commands, and optional JSON inventory or routing results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can suggest skill combinations and installation steps without automatically installing missing skills.]

## Skill Version(s):

0.29.4 (source: skill frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
