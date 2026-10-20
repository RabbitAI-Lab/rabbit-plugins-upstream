## Description:

Helps agents find and hire people for physical-world tasks, post bounties, review applications, and coordinate work through RentAHuman.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to find local workers, post paid bounties, review applicants, and coordinate real-world errands or events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posting a bounty can commit to paid real-world work without an enforced preview or approval step.

Mitigation: Require operator approval of the exact amount, worker or destination, and intended action before posting bounties or accepting applicants; apply spending limits.

Risk: The API reference describes wallet, credential, crypto, and webhook actions with financial or access consequences.

Mitigation: Use revocable API keys and require explicit operator approval before releasing payment, withdrawing funds, creating API keys, funding wallets, or registering webhooks.

## Reference(s):

- [RentAHuman API reference](references/API.md)
- [RentAHuman](https://rentahuman.ai)
- [ClawHub skill release](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browsing is public; posting bounties and messaging require a RentAHuman API key.]

## Skill Version(s):

3.16.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
