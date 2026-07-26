## Description: <br>
Basic BNB Chain operations: check balances, send BNB, and send BEP-20 tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawzai](https://clawhub.ai/user/clawzai) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and blockchain operators use this skill to inspect BNB Chain balances, inspect transactions, derive a wallet address from a private key, and submit BNB or BEP-20 transfers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend real cryptocurrency using raw private keys without strong safeguards. <br>
Mitigation: Use only a dedicated low-balance wallet and manually verify the network, token contract, recipient, and amount before any send command. <br>
Risk: Private keys can be exposed when passed on the command line or handled casually. <br>
Mitigation: Prefer a protected secret mechanism or environment variable and avoid entering private keys directly in shell history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clawzai/skills/bnb-chain) <br>
- [Publisher profile](https://clawhub.ai/user/clawzai) <br>
- [Default BNB Chain RPC endpoint](https://bsc-dataseed.binance.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and ethers.js; signing commands use BNB_PRIVATE_KEY or an explicit --key value.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
