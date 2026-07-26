## Description: <br>
Send and receive KAS cryptocurrency, check balances, send payments, and generate wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manyfestation](https://clawhub.ai/user/manyfestation) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers can use this skill to operate a Kaspa command-line wallet from an agent workflow, including balance checks, fee estimates, payment URI generation, mnemonic generation, and KAS transfers with JSON command output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can directly sign and broadcast irreversible cryptocurrency transfers using wallet secrets without a clearly documented confirmation or dry-run safeguard. <br>
Mitigation: Use a test wallet first, manually verify every recipient address, amount, network, and fee, and do not allow automated sends unless an explicit confirmation or dry-run step is added. <br>
Risk: Wallet private keys or mnemonics are supplied through environment variables that may be accessible to an agent process. <br>
Mitigation: Avoid storing valuable keys or mnemonics in long-lived environment variables, keep secrets out of logs, and scope wallet credentials to the shortest practical session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manyfestation/skills/trial) <br>
- [Kaspa mainnet transaction explorer](https://explorer.kaspa.org/txs/{txid}) <br>
- [Kaspa testnet transaction explorer](https://explorer-tn10.kaspa.org/txs/{txid}) <br>
- [Kaspa Python SDK on PyPI](https://pypi.org/project/kaspa/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with shell commands; wallet commands return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command output uses exit code 0 for success and 1 for errors; transfer actions can sign and broadcast transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
