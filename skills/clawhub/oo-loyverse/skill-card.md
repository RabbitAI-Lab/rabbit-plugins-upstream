## Description:

Loyverse (loyverse.com). Use this skill for ANY Loyverse request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read Loyverse business data through an OOMOL-connected account, including merchant profiles, stores, categories, items, customers, and receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer code from OOMOL directly in a shell.

Mitigation: Review before installing, prefer a verified and versioned oo CLI installation channel when possible, and run setup commands only after an actual authentication or connection failure.

Risk: Connecting Loyverse grants OOMOL access to read-only business data available through the connector.

Mitigation: Connect Loyverse only when that access is acceptable for the account and data being queried.

## Reference(s):

- [Loyverse homepage](https://loyverse.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Loyverse ClawHub page](https://clawhub.ai/oomol/skills/oo-loyverse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
