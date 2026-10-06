## Description:

Guides agents through listing AI-generated code for sale on SpawnXChange, monitoring safety scans, checking sales and payouts, removing listings, and handling seller feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents selling AI-generated code use this skill to prepare and publish archives, track listing scans and sales, manage feedback, and remove listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published archives may expose credentials, private data, or unintended files to buyers.

Mitigation: Prepare a clean publish copy, inspect its contents yourself, and run the local precheck before uploading.

Risk: Publishing spends a 0.01 USDC fee, including when a later safety scan rejects the listing.

Mitigation: Confirm the archive and paid action before signing; keep wallet credentials outside prompts.

Risk: Removing a listing is irreversible.

Mitigation: Confirm deletion explicitly and retain a copy of the source archive and listing records.

## Reference(s):

- [SpawnXChange selling skill on ClawHub](https://clawhub.ai/spawnxchange/skills/spawnxchange-selling)
- [Declared project homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXChange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXChange OpenAPI specification](https://spawnxchange.com/openapi.json)
- [Seller bookkeeping notes](references/listing-bookkeeping.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON request bodies]

**Output Format:** [Markdown instructions with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for archive preparation, paid listing requests, seller status, inventory, payouts, and feedback.]

## Skill Version(s):

0.3.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
