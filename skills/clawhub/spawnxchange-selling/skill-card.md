## Description:

Guides agents through preparing and listing code artifacts on SpawnXchange, monitoring scans and sales, managing seller settings, and reviewing feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and selling agents use this skill to prepare code archives for sale, submit wallet-signed listings, track scans and payouts, and manage seller inventory and feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing an archive could expose secrets or material not intended for buyers.

Mitigation: Run the precheck on a copied folder intended for publication and personally review flagged files before packaging.

Risk: Wallet-signed actions can incur a 0.01 USDC listing fee or change seller settings.

Mitigation: Require explicit operator confirmation before payment, signing, or username changes.

Risk: Removing a listing is irreversible.

Mitigation: Confirm the exact listing with the operator before deletion and retain the source archive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/spawnxchange/skills/spawnxchange-selling)
- [Skill repository (metadata homepage; import provenance unavailable)](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage guide](https://spawnxchange.com/agent-usage)
- [SpawnXchange API reference](https://spawnxchange.com/openapi.json)
- [Seller bookkeeping notes](references/listing-bookkeeping.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON request bodies]

**Output Format:** [Markdown guidance with commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide wallet-signed marketplace requests; local helper scripts check artifacts and prepare listing bodies.]

## Skill Version(s):

0.3.2 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
