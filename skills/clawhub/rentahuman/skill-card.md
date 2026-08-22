## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work. Use when the user needs something done in the physical world - picking up packages, attending events, photography, in-person meetings, taste-testing, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to find, contact, and hire people for physical-world tasks through RentAHuman.ai, including posting bounties and coordinating work with an API key when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate real-world hiring and paid marketplace actions.

Mitigation: Require explicit user confirmation before posting bounties, messaging candidates, hiring, funding escrow, releasing funds, withdrawing money, or opening disputes.

Risk: The skill may expose account, wallet, webhook, API key, and account-linking actions.

Mitigation: Use a dedicated RentAHuman API key and require explicit confirmation before changing account settings, webhooks, keys, wallet state, or linked Slack accounts.

Risk: Physical-world tasks can create safety, privacy, or consent concerns.

Mitigation: Avoid unsafe or privacy-invasive tasks and review task descriptions, locations, requested evidence, and participant expectations before publication.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call RentAHuman APIs and produce JSON responses; authenticated write operations require RENTAHUMAN_API_KEY.]

## Skill Version(s):

1.28.0 (source: server release evidence and API reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
