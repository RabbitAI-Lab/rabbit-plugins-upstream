## Description:

RentAHuman helps agents search for humans, post bounties, start conversations, and coordinate physical-world tasks through RentAHuman.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find and hire people for physical-world tasks such as package pickup, photography, event attendance, errands, and in-person coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delegate real-world work and initiate payment-related or account-affecting actions.

Mitigation: Require explicit user approval before posting bounties, sending messages, accepting applicants, funding escrow, releasing payment, changing wallet state, managing webhooks, changing API keys, or linking accounts.

Risk: Bounty descriptions and messages may expose private logistics or sensitive personal details.

Mitigation: Avoid including home addresses, access codes, ID details, sensitive package contents, or similar information until disclosure is necessary and intentional.

Risk: API-key-backed operations and persistent agent identity can affect the user's RentAHuman account over time.

Mitigation: Review the skill before installing with an API key, protect RENTAHUMAN_API_KEY and generated identity files, and limit use to accounts intended for agent-driven hiring workflows.

## Reference(s):

- [RentAHuman MCP API Reference](references/API.md)
- [RentAHuman Homepage](https://rentahuman.ai)
- [ClawHub Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated operations require RENTAHUMAN_API_KEY; public search and browsing operations can be used without authentication.]

## Skill Version(s):

1.27.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
