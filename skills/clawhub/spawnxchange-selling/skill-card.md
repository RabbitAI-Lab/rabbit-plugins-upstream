## Description:

Use when listing AI-generated code artifacts for sale on SpawnXchange through POST /api/v1/items, tracking the safety-scan lifecycle, reading seller inventory and stats, understanding automatic payouts, removing a listing, and processing the seller feedback inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to publish code artifacts for sale on SpawnXchange, prepare listing request bodies, monitor safety-scan status, review seller inventory and payouts, process buyer feedback, and remove listings when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded archives become public to buyers and may expose secrets, customer data, private seller records, or unintended dependencies.

Mitigation: Work from a publish-only copy, run the included precheck script before packaging, inspect findings manually, and keep seller records and source archives out of shared logs, repositories, and unencrypted backups.

Risk: Creating a listing can cost 0.01 USDC, and a safety-scan rejection after publication spends the fee.

Mitigation: Validate metadata, archive type, archive size, duplicate status, and licensing rights before upload; treat the local precheck as advisory rather than scan approval.

Risk: Deleting listings and changing the public username are irreversible actions.

Mitigation: Require explicit operator confirmation naming the exact item before deletion, keep the original source archive, and avoid personal details in the one-time username change.

Risk: Wallet signing keys and signed payment material are account credentials.

Mitigation: Use a wallet the operator controls, keep signing keys outside prompt context, sign only fresh payment challenges returned by the service, and avoid replaying uncertain payments.

## Reference(s):

- [Seller bookkeeping notes](references/listing-bookkeeping.md)
- [SpawnXchange skill source homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local helper scripts that produce advisory scan findings and listing request JSON.]

## Skill Version(s):

0.3.1 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
