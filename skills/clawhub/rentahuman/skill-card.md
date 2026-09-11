## Description:

RentAHuman helps agents search available humans by skill, post bounties, start conversations, and coordinate physical-world tasks such as package pickup, event attendance, photography, in-person meetings, and taste testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to find, hire, message, or coordinate humans for real-world work through RentAHuman.ai. It supports public browsing without authentication and authenticated marketplace actions such as bounties, applications, conversations, and payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated use can create paid marketplace listings, act on applications, and trigger payment-related workflows.

Mitigation: Require explicit operator review and confirmation before posting bounties, accepting applications, funding escrow, releasing payment, depositing wallet funds, or sending money.

Risk: Task descriptions and messages may contain addresses, package details, location data, or other personal information.

Mitigation: Share only the minimum information required for the task and manually review every message, bounty description, location, package detail, and attachment before submission.

Risk: The bundled API reference exposes broader account, wallet, payment, identity, webhook, and support capabilities than the main skill description highlights.

Mitigation: Limit installed usage to trusted workflows, keep RENTAHUMAN_API_KEY secret, and monitor account and wallet activity after authenticated agent use.

## Reference(s):

- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce RentAHuman API request examples and summarize JSON API responses; authenticated write, messaging, bounty, and payment actions require operator review.]

## Skill Version(s):

3.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
