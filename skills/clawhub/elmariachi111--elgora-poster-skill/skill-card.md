## Description:

Draft, review, publish, fund and follow an Elgora bounty challenge (bounty_challenge.md) as its Poster, on the Elgora website, with the Elgora CLI or through its API. Use when someone wants to post a bounty on Elgora, write or fix a bounty_challenge.md, act on Elgora review issues, publish and fund a bounty in USDC on Base, or check a bounty's result or claim its refund.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elmariachi111](https://clawhub.ai/user/elmariachi111)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft and revise Elgora bounty challenge Markdown, prepare it for review, and follow publication, funding, result, and refund steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and medium confidence because some local references could not be resolved; a clean verdict does not guarantee the skill is risk-free.

Mitigation: Review the unresolved local references and the skill's behavior before installing or using it.

Risk: Publishing a mainnet bounty escrows real USDC from the Poster's wallet.

Mitigation: Have the Poster confirm the challenge, network, and escrow amount before funding; use testnet when testing.

Risk: Wallet secrets could authorize signatures or transfers if disclosed.

Mitigation: Keep private keys and seed phrases in the wallet or host secret store, and never disclose them to Elgora or anyone else.

## Reference(s):

- [Elgora Poster Examples](https://docs.elgora.ai/docs/poster/examples)
- [Elgora Documentation](https://docs.elgora.ai)
- [Elgora Deployment Details](https://elgora.ai/deployments.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, API calls]

**Output Format:** [Markdown bounty drafts and review guidance, with optional shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A bounty_challenge.md draft with optional review, publishing, funding, and follow-up guidance.]

## Skill Version(s):

6.2.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
