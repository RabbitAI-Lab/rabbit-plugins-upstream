## Description: <br>
Launch, buy, and sell tokens on BitAgent bonding curves via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parasyte-x](https://clawhub.ai/user/parasyte-x) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to launch BitAgent bonding-curve tokens and submit buy or sell trades on BSC Mainnet or BSC Testnet through a CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a stored wallet private key to submit real blockchain launches and trades. <br>
Mitigation: Use a dedicated low-balance wallet, keep PRIVATE_KEY out of shared configs, logs, and source control, and require explicit human approval before every mainnet launch, buy, or sell. <br>
Risk: Blockchain launches and trades can be irreversible and may lose funds. <br>
Mitigation: Start on BSC Testnet, verify the token address, amount, network, repository, and npm dependencies before use, and limit mainnet exposure. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parasyte-x/skills/openclaw-bitagent) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [BitAgent Mainnet App](https://app.bitagent.io) <br>
- [BitAgent Testnet App](https://testnet.app.bitagent.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [CLI stdout returned as text, with setup guidance in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Launch returns a contract address and URL; buy and sell return transaction hashes.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
