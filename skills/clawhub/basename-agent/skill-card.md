## Description: <br>
Basename Agent helps agents register a Basename on Base and create a BaseMail email through Donate Buy, worker-paid auto registration, or WalletConnect v2. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daaab](https://clawhub.ai/user/daaab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to obtain an onchain Base identity and BaseMail address, either through direct API and contract calls or through WalletConnect-driven registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet signing and auto-approval behavior could authorize actions outside the identity-registration goal. <br>
Mitigation: Use a low-value dedicated wallet, enable interactive confirmations, and inspect every message, transaction recipient, calldata, and value before signing. <br>
Risk: WalletConnect flows can connect to arbitrary dApps unless constrained. <br>
Mitigation: Limit use to trusted origins and add contract, origin, calldata, and value allowlists before broader deployment. <br>
Risk: The skill requires private-key-backed wallet automation for some paths. <br>
Mitigation: Store private keys only in environment variables, avoid shell arguments, and fund the wallet only with the amount needed for the intended transaction. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/daaab/skills/basename-agent) <br>
- [BaseMail](https://basemail.ai) <br>
- [BaseMail API Docs](https://api.basemail.ai/api/docs) <br>
- [DonateBuy Contract on BaseScan](https://basescan.org/address/0x8b10c4D29C99Eac19Edc59C4fac790518b815DE7#code) <br>
- [AttentionBondEscrow on BaseScan](https://basescan.org/address/0xF5fB1bb79D466bbd6F7588Fe57B67C675844C220#code) <br>
- [CO-QAF and Attention Bonds](https://blog.juchunko.com/en/glen-weyl-coqaf-attention-bonds/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown instructions with Bash, JavaScript, and Python examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet setup guidance and commands that may initiate signing or onchain transactions when run by the user.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence; artifact/_meta.json reports 2.1.0 and artifact/package.json reports 1.6.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
