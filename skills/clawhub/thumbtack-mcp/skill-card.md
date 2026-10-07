## Description:

Helps agents search public Thumbtack listings and read local service professional profiles from a shell without signing in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up public local service professionals by trade and ZIP code, then inspect their profiles, ratings, reviews, and service details without an account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live searches send service and location queries to Thumbtack from the user's machine.

Mitigation: Avoid sensitive searches and use the skill only when external requests are acceptable.

Risk: Generated shell commands, especially GraphQL POST bodies, may make unintended external requests if run unchecked.

Mitigation: Review the commands and request bodies before running them.

## Reference(s):

- [Thumbtack discovery recipes](references/discovery.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public listings; search and profile data may vary by location and availability.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
