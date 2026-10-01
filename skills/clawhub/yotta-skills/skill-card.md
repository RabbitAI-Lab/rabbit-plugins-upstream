## Description:

Helps agents recommend combinations of YottaMeta skills, inspect installed skills, and provide commands for installing and updating the skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to choose YottaMeta skills for a task, inspect their installed skills, and preview or run family installations and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or updates can persistently add or replace skills without reliably enforcing the documented confirmation step.

Mitigation: Review the proposed changes and obtain explicit approval; pin the package version, run --dry-run, and test with --dir before changing an agent's skills.

Risk: Package lifecycle checks or scripts may run during installation, and full-family or automatic updates extend trust to more packages.

Mitigation: Inspect the packages and install plan, avoid --skip-scan, and reserve update --auto or family-wide installation for deliberately approved use.

Risk: Optional MCP, global memory text, and local providers create persistent integrations.

Mitigation: Leave these integrations disabled unless the user explicitly requests and reviews them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage listed in skill metadata](https://github.com/YottaMeta/yotta-skills)
- [Installation workflow](references/install-flow.md)
- [Orchestration guide](references/orchestration.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing and memory decisions are recommendations; install and update commands can change local skills.]

## Skill Version(s):

0.23.2 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
