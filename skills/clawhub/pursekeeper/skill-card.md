## Description:

Helps agents earn, hold, and spend Nano (XNO) through a no-node wallet, HTTP 402 payment examples, and a directory of Nano-accepting services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to set up a Nano wallet without running a node, pay Nano-priced APIs, find services that accept Nano, and offer services paid through HTTP 402.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet operations sign using remote account data that may silently change the account representative.

Mitigation: Use a trusted account-info or RPC endpoint and verify or locally control the representative before signing.

Risk: Disclosure of the wallet seed can expose funds.

Mitigation: Keep NANO_SEED out of logs and persistent shell history, and hold only small balances.

Risk: Paid calls can spend more Nano than intended.

Mitigation: Review each payment quote and set NANO_MAX_PAY deliberately for each paid call.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [Pursekeeper website and API](https://pursekeeper.dev)
- [No-node wallet and payment guide](references/no-node.md)
- [Nano seller directory](references/sellers.md)
- [NanoGPT payment guide](references/buy-from-nanogpt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment instructions and transaction receipts may include public Nano addresses and block hashes.]

## Skill Version(s):

0.1.14 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
