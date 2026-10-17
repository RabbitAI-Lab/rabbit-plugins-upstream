## Description:

Guides developers using an unofficial Go client to read Trading 212 account data and integrate order and pie operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add an unofficial Trading 212 client for account summaries, positions, history, orders, and pies. Account-changing actions require an explicit user request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated integrations can place or cancel real-money orders and modify account pies.

Mitigation: Start with the demo environment and require clear confirmation before each live order, cancellation, or pie change.

Risk: Exposed API credentials could grant access to the trading account.

Mitigation: Read the API key and secret from environment variables; never hardcode, commit, or log them.

## Reference(s):

- [Go Trading212 skill release](https://clawhub.ai/psyb0t/skills/go-trading212)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples default to the demo environment; live account changes require explicit user confirmation.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
