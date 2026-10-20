## Description:

Helps agents earn, hold, and spend Nano (XNO) through a wallet, a directory of paid services, and HTTP 402 payment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Pursekeeper to manage a Nano wallet, find services that accept Nano, pay for API calls, and offer paid services to other agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using a wallet seed can spend real funds, and confirmed payments cannot be reversed.

Mitigation: Use a dedicated low-balance wallet and set NANO_MAX_PAY and NANO_CAP deliberately before paying.

Risk: Exposing the wallet seed or an unprotected local payment proxy can put funds at risk.

Mitigation: Keep NANO_SEED out of logs and shared files, and set a strong PROXY_KEY before running the proxy.

Risk: Third-party paid services receive submitted prompts, files, or business data.

Mitigation: Review each service endpoint and the data it will receive before making a paid request.

## Reference(s):

- [Pursekeeper on ClawHub](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Nano wallet guide](references/no-node.md)
- [Nano payment service directory](references/sellers.md)
- [NanoGPT purchase guide](references/buy-from-nanogpt.md)
- [Inference proxy guide](references/inference-proxy.md)
- [Live seller directory](https://pursekeeper.dev/sellers.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nano addresses and transaction receipts.]

## Skill Version(s):

0.3.4 (source: frontmatter, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
