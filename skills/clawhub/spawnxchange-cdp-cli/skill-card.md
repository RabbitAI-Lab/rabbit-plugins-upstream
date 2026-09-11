## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a wallet managed by the Coinbase Developer Platform (CDP) CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to buy, download, list, and manage AI-generated code artifacts on SpawnXchange with a CDP-managed wallet. It is intended for workflows that require explicit x402 payment signing, marketplace account actions, and large archive uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid marketplace requests can spend USDC if the operator signs an x402 payment.

Mitigation: Require explicit operator intent, set tight payment limits with --max-amount-raw, and verify the item, price, network, and recipient before executing paid requests.

Risk: Listing an archive can publish unintended secrets, customer data, dependency caches, or unrelated project files.

Mitigation: Package from a clean copy, review archive contents before upload, and exclude .env files, credentials, customer data, dependency directories, build caches, and unrelated files.

Risk: Deleting a listing is irreversible and removes it from future discovery.

Mitigation: Confirm the exact item ID and title with the operator before deletion, and keep a local copy of seller archives and records.

Risk: Download and invoice URLs are short-lived bearer links.

Mitigation: Fetch purchased artifacts and invoices promptly, avoid logging or sharing links, and keep order IDs so fresh links can be requested when needed.

## Reference(s):

- [SpawnXchange skills repository](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)
- [Coinbase Developer Platform CLI skill](https://docs.cdp.coinbase.com/cdp-cli/skill.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires cdp, curl, jq, tar, and python3 on PATH; examples use a user-provided CDP wallet address.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
