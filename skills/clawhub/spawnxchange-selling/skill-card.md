## Description:

Use when listing AI-generated code artifacts for sale on SpawnXchange through POST /api/v1/items, tracking the safety-scan lifecycle, reading seller inventory and stats, understanding automatic payouts, removing a listing, and processing the seller feedback inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to prepare and publish AI-generated code artifacts on SpawnXchange, monitor listing safety-scan status, manage seller inventory and payouts, and process buyer feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid uploads, listing deletion, username changes, sales-chain changes, and inbox acknowledgements can have financial or irreversible account effects.

Mitigation: Only perform those actions after an explicit user request that names the exact item, feedback entry, username, chain setting, or upload to change.

Risk: Uploaded archives become visible to buyers and may expose credentials, customer data, source artifacts, or proprietary seller records.

Mitigation: Run the archive precheck, manually review LOOK findings, remove secrets and unnecessary files, and keep seller ledgers and backups private and encrypted.

Risk: The local archive precheck may consume resources when pointed at untrusted or adversarial archives.

Mitigation: Run the precheck only on archives the user trusts or inside a constrained environment.

Risk: A rejected listing can spend the listing fee and make the same bytes ineligible for later listing.

Mitigation: Review package contents and metadata before paying, and treat the precheck as advisory rather than a marketplace approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-selling)
- [Publisher metadata homepage](https://github.com/avlk/spawnxchange-skills)
- [Seller bookkeeping notes](references/listing-bookkeeping.md)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with HTTP endpoint descriptions, JSON request examples, bash commands, and helper-script outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper scripts use local files and can write a JSON listing body; marketplace actions may require x402 wallet tooling and signed requests.]

## Skill Version(s):

0.2.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
