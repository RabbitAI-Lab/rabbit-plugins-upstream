## Description: <br>
Complete OpenClaw-ready operating skill for @moltmoon/sdk V2. Use when an agent needs to install, configure, and operate the MoltMoon SDK or CLI end-to-end on Base mainnet, including launch dry-runs, metadata/image validation, live token launches, quote checks, buys, sells, rewards claiming, migration, troubleshooting, and safe production runbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chillbruhhh](https://clawhub.ai/user/chillbruhhh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to configure and operate the MoltMoon SDK or CLI on Base mainnet for token launches, dry-runs, trading, rewards claims, migration checks, troubleshooting, and production runbooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live Base mainnet launches, trades, claims, migrations, and approvals using a wallet private key. <br>
Mitigation: Use a dedicated wallet with limited funds and require manual confirmation of wallet, chain, addresses, amounts, slippage, approvals, and transaction hashes before each write action. <br>
Risk: Installing or running @moltmoon/sdk without version pinning can expose the operator to unexpected package changes. <br>
Mitigation: Pin and verify the @moltmoon/sdk package version before use, especially before live transactions. <br>
Risk: Private-key handling creates risk of credential exposure or unintended signing authority. <br>
Mitigation: Keep keys in local secrets or environment variables, never commit them, and avoid using wallets that hold valuable assets. <br>


## Reference(s): <br>
- [MoltMoon Crypto Launcher on ClawHub](https://clawhub.ai/chillbruhhh/skills/moltmoon-agentcrypto-sdk) <br>
- [MoltMoon API endpoint](https://api.moltmoon.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, env, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run and live-operation runbooks for Base mainnet actions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
