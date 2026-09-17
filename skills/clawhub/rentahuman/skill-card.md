## Description:

Hire humans for physical-world tasks via RentAHuman.ai, including searching profiles, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find human workers, post and manage paid bounties, message applicants, and coordinate physical-world tasks such as package pickup, photography, event attendance, errands, and testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated operations can post bounties, accept applications, message workers, and move funds.

Mitigation: Require explicit user confirmation before bounties, messages, application decisions, checkout, escrow, payment release, wallet, or transfer actions; preview costs and counterparties first.

Risk: Tasks may involve locations, schedules, identity, payment context, or other sensitive personal details.

Mitigation: Collect only details necessary for the task, keep API keys out of prompts and logs, and avoid passwords, OTPs, private keys, bank or card details, exact home addresses, dates of birth, and government IDs unless strictly required by the platform workflow.

Risk: Server security evidence marks the release suspicious because high-impact real-world, payment, and account actions are not sufficiently enforced or scoped.

Mitigation: Install only for supervised workflows with a RentAHuman API key, audit requested actions before execution, and use runtime controls that limit who can approve paid or real-world actions.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman Homepage](https://rentahuman.ai)
- [ClawHub Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated write, hiring, messaging, and payment-related operations require RENTAHUMAN_API_KEY.]

## Skill Version(s):

3.6.0 (source: server release evidence, API reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
