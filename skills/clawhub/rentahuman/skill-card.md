## Description:

Hire humans for physical-world tasks through RentAHuman.ai by searching profiles, posting bounties, messaging workers, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find people with relevant skills, post paid task bounties, review applicants, message workers, and coordinate completion of physical-world work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access can post bounties, message workers, accept applications, and trigger escrow, wallet, or payment workflows.

Mitigation: Use a dedicated low-balance account or tightly limited API key when available, preview spending before posting, and require explicit operator confirmation before any hiring or payment action.

Risk: The API reference includes account, API-key, crypto, webhook, Slack-linking, wallet, and refund operations beyond basic task hiring.

Mitigation: Limit routine use to search, bounty, conversation, and application workflows; invoke broader administrative or financial tools only when the operator explicitly asks for that exact action.

Risk: Real-world work coordination can expose personal, location, payment, or credential information if task instructions are overbroad.

Mitigation: Define completion criteria and evidence types clearly, avoid requesting secrets or sensitive personal data, and review worker profiles, reviews, evidence, and costs before accepting work or releasing payment.

## Reference(s):

- [RentAHuman MCP API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only browsing can use public endpoints; bounty, messaging, account, wallet, escrow, webhook, and payment actions require RENTAHUMAN_API_KEY.]

## Skill Version(s):

3.1.0 (source: server release evidence and API reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
