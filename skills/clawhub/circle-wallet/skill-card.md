## Description: <br>
USDC wallet operations for OpenClaw agents via Circle Developer-Controlled Wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eltontay](https://clawhub.ai/user/eltontay) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to let agents create and manage Circle Developer-Controlled Wallets, check USDC balances, request sandbox testnet funds, and send USDC across supported chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move real USDC when production Circle credentials and funded wallets are configured. <br>
Mitigation: Use sandbox credentials first and require separate human confirmation for every send, including recipient, amount, network, and source wallet. <br>
Risk: Circle API keys and entity secrets are required and stored under ~/.openclaw/circle-wallet/. <br>
Mitigation: Keep credentials off shared machines and logs, verify local file permissions, and rotate credentials if exposure is suspected. <br>
Risk: Reconfiguration or setup can clear local wallet metadata such as saved wallets and defaults. <br>
Mitigation: Back up wallet metadata before setup or reconfiguration, especially before switching between sandbox and production credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/eltontay/skills/circle-wallet) <br>
- [Circle Developer Docs](https://developers.circle.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style agent responses with inline shell commands and CLI output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform Circle wallet API calls and local configuration file updates when commands are executed.] <br>

## Skill Version(s): <br>
1.0.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
