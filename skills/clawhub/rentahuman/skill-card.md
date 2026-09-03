## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching available humans, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find and hire people for physical-world work such as package pickup, photography, event attendance, errands, service bookings, and evidence-based task completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API surface includes payment, wallet, escrow, account, webhook, crypto-key, and private-data workflows.

Mitigation: Review the full API surface before installing and use a least-privilege RentAHuman API key.

Risk: Authenticated actions can post bounties, message workers, accept applications, spend or release funds, create webhooks, change API keys, or share private task details with third-party humans.

Mitigation: Require clear user confirmation before any sensitive, external, or financial action.

Risk: Crypto-funded account or wallet actions may require an x402 private key.

Mitigation: Do not expose an x402 private key unless the operator explicitly intends to use crypto-funded workflows.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill listing](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash examples and a Node.js CLI script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only search can use public endpoints; authenticated actions require RENTAHUMAN_API_KEY.]

## Skill Version(s):

3.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
