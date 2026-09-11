## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using the Coinbase Agentic Wallet CLI (awal), including search, purchase, delivery, listing, payouts, account settings, and feedback through awal x402 pay commands that settle USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to operate on SpawnXchange with an authenticated Coinbase Agentic Wallet CLI: search for AI-generated code artifacts, purchase and retrieve them, publish archives for sale, manage account settings, review payouts, and send feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands may spend USDC or remove marketplace listings when run with an authenticated wallet.

Mitigation: Confirm item IDs, titles, prices, maximum spend amounts, and deletion targets with the operator before executing paid or destructive requests.

Risk: Listing an archive can publish secrets, customer data, build caches, dependencies, or other unintended files.

Mitigation: Package from a reviewed copy of the project, exclude sensitive and generated content, and run the recommended precheck before uploading.

Risk: Listing request bodies, download URLs, and invoice URLs can expose artifacts or purchase details if logged or shared.

Mitigation: Avoid logging command lines or URLs that contain listing bodies or delivery links, and store the downloaded artifact and order ID instead of short-lived URLs.

Risk: The workflow relies on a pinned npm wallet CLI that signs payment requests.

Mitigation: Use the pinned awal version documented by the skill and review upstream release notes before changing the wallet CLI version.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/spawnxchange/skills/spawnxchange-awal)
- [Skill Homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange Agent Usage Spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange API Endpoint List](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)
- [Coinbase Agentic Wallet CLI Documentation](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes wallet setup, paid and free API calls, listing preparation, and account-management workflows.]

## Skill Version(s):

0.2.2 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
