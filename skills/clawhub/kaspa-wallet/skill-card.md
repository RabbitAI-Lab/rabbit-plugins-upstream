## Description: <br>
Send and receive KAS cryptocurrency, check balances, send payments, and generate wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manyfestation](https://clawhub.ai/user/manyfestation) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to interact with a Kaspa wallet from the command line, including checking balances, estimating fees, generating wallet material, creating payment URIs, and sending KAS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend real KAS from configured wallet secrets without an explicit confirmation step. <br>
Mitigation: Use a small dedicated wallet or testnet first, and require separate human approval before running any send or max transaction. <br>
Risk: Private keys or mnemonics supplied through environment variables could be exposed in shared shells, command history, or logs. <br>
Mitigation: Keep wallet secrets out of shared shells and logs, avoid primary seed phrases, and unset secret variables after use. <br>
Risk: The installer resolves and installs the kaspa Python package from PyPI. <br>
Mitigation: Review the resolved package before deployment and pin or mirror the dependency according to local supply-chain controls. <br>


## Reference(s): <br>
- [Kaspa Wallet on ClawHub](https://clawhub.ai/manyfestation/skills/kaspa-wallet) <br>
- [Kaspa Mainnet Explorer](https://explorer.kaspa.org/txs/{txid}) <br>
- [Kaspa Testnet Explorer](https://explorer-tn10.kaspa.org/txs/{txid}) <br>
- [Kaspa Python SDK on PyPI](https://pypi.org/project/kaspa/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Command-line JSON responses with Markdown usage guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands return exit code 0 on success and 1 on error; wallet credentials are supplied through environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
