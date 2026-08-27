## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find, hire, message, and coordinate human workers for real-world tasks such as package pickup, event attendance, photography, errands, and taste-testing. It supports public browsing without authentication and authenticated account actions for posting bounties, conversations, applications, escrow, wallet, webhook, and identity workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated account actions can post bounties, message workers, accept applications, manage escrow or wallet flows, create webhooks, link Slack accounts, change API keys, or use x402 features.

Mitigation: Require explicit user confirmation before each account, payment, messaging, webhook, Slack, API-key, escrow, wallet, or x402 action, and use an API key with spending limits where available.

Risk: Real-world task details may expose sensitive personal information such as addresses, package numbers, schedules, IDs, or location-specific instructions.

Mitigation: Share only the minimum details needed for the specific task, redact unnecessary sensitive information, and confirm with the user before sending private or location-sensitive data.

Risk: Persistent agent identities and API credentials can continue to affect the same RentAHuman account across sessions.

Mitigation: Use purpose-specific identities and API keys, store credentials securely, rotate or revoke keys after use, and avoid delegating keys the user is not comfortable exposing to the agent.

## Reference(s):

- [RentAHuman Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)
- [RentAHuman Homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples, Node.js command examples, API descriptions, and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated operations require RENTAHUMAN_API_KEY; public search and profile browsing do not require authentication.]

## Skill Version(s):

1.29.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
