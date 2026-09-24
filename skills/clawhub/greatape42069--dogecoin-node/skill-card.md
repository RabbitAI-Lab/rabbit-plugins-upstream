## Description:

A skill to set up and operate a Dogecoin Core full node with RPC access, blockchain tools, and optional tipping functionality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[greatape42069](https://clawhub.ai/user/greatape42069)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to configure and monitor a Dogecoin Core node, issue Dogecoin RPC commands, check wallet activity, and optionally manage a local SQLite tipping workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The send command can transfer real DOGE without an explicit confirmation step.

Mitigation: Require manual transaction confirmation and validate recipient addresses and amounts before any send operation.

Risk: The setup flow downloads wallet-related Dogecoin binaries.

Mitigation: Verify downloaded binaries against official checksums or signatures before installation or execution.

Risk: The skill interacts with wallet data and may expose wallet/account state.

Mitigation: Use only wallets or accounts that are acceptable to expose to the skill and avoid using high-value wallets.

Risk: Scheduled health scripts in mutable workspace paths can be abused if file ownership or permissions are weak.

Mitigation: Lock down permissions and ownership before scheduling any generated or workspace-hosted scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/greatape42069/skills/dogecoin-node)
- [Publisher profile](https://clawhub.ai/user/greatape42069)
- [Dogecoin Core 1.14.9 Linux binary](https://github.com/dogecoin/dogecoin/releases/download/v1.14.9/dogecoin-1.14.9-x86_64-linux-gnu.tar.gz)
- [CoinGecko Dogecoin price API](https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd)
- [Dogecoin RPC command cheat sheet](artifact/RPC_CHEATSHEET.md)
- [Dogecoin node heartbeat](artifact/HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash and Python code blocks; runtime commands return text and RPC-derived CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may interact with a local Dogecoin wallet, local filesystem paths, localhost RPC, GitHub downloads, CoinGecko, and SQLite.]

## Skill Version(s):

1.0.5 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
