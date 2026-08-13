## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching available workers, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find and hire people for physical-world tasks such as package pickup, event attendance, photography, errands, taste testing, and in-person coordination. Authenticated users can create bounties, message workers, manage applications, and coordinate payments through RentAHuman.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated operations can post bounties, message workers, fund escrow, send money, change API keys, or create webhooks.

Mitigation: Require explicit user confirmation before any authenticated action that creates work, contacts a worker, changes account settings, registers a webhook, or moves funds.

Risk: Real-world task coordination can expose sensitive addresses, schedules, package identifiers, documents, and identity details.

Mitigation: Share only the minimum task details needed for the chosen worker or bounty, and avoid unnecessary personal, location, document, or schedule information.

Risk: Granting an API key gives the agent broad account-scoped RentAHuman capabilities.

Mitigation: Use only an account and API key the user is comfortable delegating, review the skill before installation, and revoke or rotate keys when access is no longer needed.

## Reference(s):

- [RentAHuman MCP API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only browsing can be performed without an API key; authenticated write, payment, account, and webhook operations require RENTAHUMAN_API_KEY.]

## Skill Version(s):

1.24.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
