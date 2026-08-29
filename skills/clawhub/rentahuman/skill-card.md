## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find available people for real-world tasks, review profiles, post bounties, and coordinate task conversations through RentAHuman.ai.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to involve outside humans in physical-world tasks.

Mitigation: Install only when that behavior is intended, and require explicit confirmation before posting bounties, messaging workers, accepting applications, or coordinating task execution.

Risk: The skill documents financial, credential, account, identity-linking, webhook, and crypto-flow capabilities.

Mitigation: Use a limited RentAHuman API key and require explicit confirmation before payments, API key creation, account linking, webhook registration, or x402 crypto flows.

Risk: Real-world task coordination can expose sensitive personal information.

Mitigation: Avoid sharing home addresses, package identifiers, schedules, private documents, government IDs, credentials, or other sensitive details unless strictly necessary.

## Reference(s):

- [RentAHuman.ai](https://rentahuman.ai)
- [API Reference](references/API.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands, Node.js CLI commands, API payloads, and configuration guidance for RENTAHUMAN_API_KEY.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
