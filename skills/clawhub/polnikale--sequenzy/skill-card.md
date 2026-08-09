## Description:

Sequenzy helps agents choose safe Sequenzy CLI and MCP workflows for account, subscriber, campaign, sequence, transactional email, integration, reporting, and configuration operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to select the right Sequenzy workflow, verify authentication, inspect resources, and carry out supported marketing, subscriber, automation, reporting, and configuration tasks with appropriate safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through authenticated Sequenzy account operations, including campaign, subscriber, team, webhook, integration, API-key, and publishing workflows.

Mitigation: Use explicit human confirmation before mutations such as cancellation, deletion, API-key revocation, team changes, webhook or integration changes, and public publishing.

Risk: The security summary notes campaign cancellation behavior that may occur before clarifying questions.

Mitigation: Inspect campaign state first and require the user to confirm the exact campaign and intended cancellation before executing cancellation commands.

Risk: Feedback or operational reports could include secrets or sensitive customer information.

Mitigation: Redact API keys, signing secrets, customer details, and confidential campaign content before submitting feedback or sharing reports.

## Reference(s):

- [Command Reference](references/command-reference.md)
- [Use Cases](references/use-cases.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dashboard URLs, safety checks, and CLI or MCP caveats when relevant.]

## Skill Version(s):

1.6.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
