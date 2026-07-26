## Description: <br>
Base Wallet helps agents create Base/Ethereum wallets, sign SIWE messages, check balances, send transactions, and register with BaseMail without browser extensions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to give an autonomous agent a Base-compatible wallet for identity, SIWE authentication, balance checks, and transaction workflows. It can also register a BaseMail address through wallet signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles wallet secrets and can expose private keys or mnemonics. <br>
Mitigation: Use a test or low-value wallet first, avoid CI and shared logs for real secrets, and keep production funds out of agent-accessible wallets unless controls are in place. <br>
Risk: The skill can sign SIWE messages, contact BaseMail.ai, and support account, email, credit, or blockchain-related actions. <br>
Mitigation: Require explicit human approval before BaseMail registration, email actions, credit purchases, or blockchain transactions. <br>
Risk: Managed wallet mode can write wallet files locally. <br>
Mitigation: Use managed storage only when needed, restrict file permissions, and keep wallet files out of version control. <br>


## Reference(s): <br>
- [Base Wallet ClawHub Release](https://clawhub.ai/daaab/skills/base-wallet) <br>
- [BaseMail API Reference](references/basemail-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command examples; scripts emit environment-variable exports, JSON, or terminal text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local wallet and audit files when the user opts into managed storage or runs scripts.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
