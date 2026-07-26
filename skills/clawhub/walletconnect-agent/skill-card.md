## Description: <br>
Walletconnect Agent lets an agent connect to Web3 dApps through WalletConnect v2 and sign supported wallet requests, including transactions and messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent connect a dedicated wallet to Web3 dApps, sign WalletConnect requests, and perform actions such as token swaps, NFT minting, DAO voting, or Basename registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority to control a crypto wallet and auto-approve blockchain actions. <br>
Mitigation: Use only a dedicated, low-value wallet, keep balances small, prefer interactive approval, and connect only to trusted dApps. <br>
Risk: A signing request or transaction may authorize unwanted spending or unsafe contract interaction. <br>
Mitigation: Review audit logs and add external safeguards such as spend limits, contract allowlists, and transaction simulation before signing. <br>
Risk: Private key exposure can compromise the wallet. <br>
Mitigation: Provide private keys through environment variables only and avoid main wallets or reusable high-value keys. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daaab/skills/walletconnect-agent) <br>
- [Base Names](https://www.base.org/names) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can guide an agent to run WalletConnect and Basename registration scripts using environment variables, command options, and audit logging.] <br>

## Skill Version(s): <br>
1.6.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
