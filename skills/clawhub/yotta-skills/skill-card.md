## Description:

YuanGe helps developers plan combinations of YottaMeta skills, inspect installed skills, and install or maintain them across supported agent directories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can ask for skill-routing suggestions, inventory installed skills, and get commands for installing, updating, or checking the YottaMeta skill family.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security report flags execution and installation weaknesses, including code running after failed checks.

Mitigation: Review the release and installation behavior before use, and avoid running it in an environment with access to sensitive files or credentials.

Risk: The supplied CLI examples use an unpinned package version, so the fetched release may change over time.

Mitigation: Pin the package version in commands and verify the package contents before installation.

Risk: The scan was partial, with limited instruction analysis and an unreadable skill manifest.

Mitigation: Treat the scan as incomplete evidence and perform a fresh review of the exact release before relying on it.

## Reference(s):

- [Skill overview on ClawHub](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project repository](https://github.com/YottaMeta/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow](references/install-flow.md)
- [Skill inventory guide](references/skill-list.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, JSON, Configuration instructions]

**Output Format:** [Markdown guidance and CLI examples, with optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing suggestions include a proposed skill order and rationale; installation commands are provided for user-directed execution.]

## Skill Version(s):

0.30.11 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
