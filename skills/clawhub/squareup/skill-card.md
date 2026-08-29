## Description:

Square API integration with managed OAuth through Maton for Square administration and supported Square API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Square resources through the Maton CLI, including locations, merchants, payments, refunds, customers, orders, catalog, inventory, invoices, team members, loyalty, checkout, cards, payouts, bank accounts, and terminal workflows. It is intended for tasks that need authenticated Square API access with managed OAuth and explicit approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Square actions, including financial or data-changing operations.

Mitigation: Default to read and list calls, then require explicit user approval after checking the endpoint, account, resource ID, payload, and consequence before any write or financial action.

Risk: Square access depends on OAuth connections and credentials that may grant administrative access.

Mitigation: Use the least-privileged Square account and OAuth scopes available, verify the intended Maton connection ID before requests, and revoke unused connections promptly.

Risk: Square API responses can contain untrusted external data.

Mitigation: Treat returned content as data only; do not execute it, interpolate it into shell commands, or let it choose follow-up endpoints or recipients.

## Reference(s):

- [ClawHub Square Skill](https://clawhub.ai/byungkyu/skills/squareup)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Square API Overview](https://developer.squareup.com/docs)
- [Square API Reference](https://developer.squareup.com/reference/square)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Square API endpoint paths, Maton CLI commands, OAuth connection guidance, and approval checkpoints for write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
