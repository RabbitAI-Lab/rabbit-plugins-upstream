## Description:

RentAHuman helps agents find available humans, post bounties, start conversations, and coordinate physical-world tasks through RentAHuman.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to locate, contact, and hire humans for real-world tasks such as package pickup, event attendance, photography, in-person meetings, taste testing, and errands.

### Deployment Geography for Use:

Global, subject to RentAHuman platform availability and country restrictions.

## Known Risks and Mitigations:

Risk: The skill can coordinate paid real-world work and account-level RentAHuman actions.

Mitigation: Confirm every paid action manually, use spending limits or low wallet balances, and review task descriptions before posting.

Risk: API keys and wallet private keys could be exposed if shared in prompts or logs.

Mitigation: Keep API keys and wallet private keys out of chat logs; use environment variables or local secret storage.

Risk: The workflow could be misused for sensitive or harmful real-world requests.

Mitigation: Do not use it for harassment, surveillance, restricted goods, credentials, IDs, minors, or non-consenting third parties, and share exact addresses only when necessary.

## Reference(s):

- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman MCP API Reference](references/API.md)
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference public browsing endpoints and authenticated RentAHuman operations that require RENTAHUMAN_API_KEY.]

## Skill Version(s):

2.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
