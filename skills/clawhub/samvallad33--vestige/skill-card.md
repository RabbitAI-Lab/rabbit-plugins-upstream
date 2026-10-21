## Description:

Vestige guides agents in recording decisions to a local memory store, recalling entries by exact handle, checking write receipts, and tracing recorded links from failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samvallad33](https://clawhub.ai/user/samvallad33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can set up a separate local Vestige MCP memory store to retain tagged decisions, look up exact entries, review write receipts, and investigate recorded failure histories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive content saved to the local memory store may persist beyond the session.

Mitigation: Do not save secrets or confidential content; use a per-project data directory when appropriate.

Risk: Global installation introduces an external npm package into the agent environment.

Mitigation: Review the upstream package before installing vestige-mcp-server globally.

## Reference(s):

- [Vestige ClawHub listing](https://clawhub.ai/samvallad33/skills/vestige)
- [Vestige MCP project documentation](https://github.com/samvallad33/vestige)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory writes return receipts; recall requires an exact memory ID or tag.]

## Skill Version(s):

4.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
