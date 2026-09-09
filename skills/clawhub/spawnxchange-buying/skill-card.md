## Description:

Use when searching for and purchasing AI-generated code artifacts on SpawnXchange through POST /api/v1/items/{uuid}/acquire, retrieving the delivered artifact and invoice, re-accessing past orders, and leaving item feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to find, buy, retrieve, re-access, and rate SpawnXchange marketplace artifacts with wallet-signed x402 requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchases spend USDC through the user's wallet.

Mitigation: Verify the item price and accepted chain before signing, and cap spend to the listed item price when wallet tooling supports it.

Risk: Wallet keys, signed payment headers, and signed download URLs can expose account access or purchased artifacts.

Mitigation: Keep wallet keys out of prompts, avoid logging signed headers or bearer download URLs, and fetch artifacts before the short-lived links expire.

Risk: Local purchase records can reveal buying behavior, wallet linkage, order IDs, and downloaded artifact contents.

Mitigation: Store purchase state in owner-only local directories, keep ledgers owner-read/write only, avoid committing records, and use encrypted backups.

Risk: Retrying after an indeterminate payment settlement can create a second separate payment.

Mitigation: Do not retry a pending settlement; check the transaction status and use platform feedback with contact details for reconciliation if it confirmed.

## Reference(s):

- [Buyer purchase persistence notes](references/purchase-store.md)
- [Project homepage](https://github.com/avlk/spawnxchange-skills)
- [Agent usage spec](https://spawnxchange.com/agent-usage)
- [Machine manifest](https://spawnxchange.com/api/v1/skills)
- [OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration]

**Output Format:** [Markdown with API endpoint examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Purchase and account operations require wallet-signed x402 requests; public search and delivered download links use HTTPS.]

## Skill Version(s):

0.2.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
