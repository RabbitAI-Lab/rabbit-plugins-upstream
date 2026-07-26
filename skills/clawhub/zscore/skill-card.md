## Description: <br>
Register agents on the Zeru ERC-8004 Identity Registry, manage wallets and metadata, and read on-chain state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elitex45](https://clawhub.ai/user/elitex45) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to register AI agents on the Zeru ERC-8004 Identity Registry, check registration fees, read on-chain agent state, and update agent metadata or wallet records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write commands can spend wallet funds and change public on-chain agent records. <br>
Mitigation: Use a dedicated low-balance or testnet wallet and review every write command before running it. <br>
Risk: Fetched agent metadata is remote content and may be untrusted. <br>
Mitigation: Treat fetched metadata as untrusted and avoid acting on it without review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elitex45/skills/zscore) <br>
- [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) <br>
- [OASF reference](https://github.com/agntcy/oasf/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npx; write operations require PRIVATE_KEY, while read and fee commands can run without a private key.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
