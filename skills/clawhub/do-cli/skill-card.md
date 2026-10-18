## Description:

Guides agents in using the do CLI to manage tasks, habits, plans, and other personal life-tracking information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to capture and review tasks, track habits, propose plans, and manage personal information through the do CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can change personal data and post messages, despite a narrower description of its capabilities.

Mitigation: Require explicit user confirmation before posting, accepting plans, canceling tasks, retiring habits, or changing areas.

Risk: An overly broad or stored API key may expose account data or permit unwanted changes.

Mitigation: Grant only necessary API-key scopes, prefer environment variables to saved credentials for agents, and confirm before reading sensitive notes or contacts.

Risk: A pipe-to-shell installer executes downloaded code without prior review.

Mitigation: Avoid the pipe-to-shell installer; use a reviewed installation method instead.

## Reference(s):

- [do skill on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [do CLI documentation and source](https://github.com/robbeverhelst/do)
- [do CLI releases](https://github.com/robbeverhelst/do/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and CLI commands; CLI responses may be JSON or readable text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a scoped API key; command results depend on the user's account and permissions.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
