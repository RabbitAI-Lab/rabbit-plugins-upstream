## Description: <br>
Create, browse, accept, and complete on-chain work requests with trade deadlines and gasless relay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[locjonz](https://clawhub.ai/user/locjonz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to create, browse, accept, coordinate, and complete on-chain work requests with escrow on Base. It supports requester and provider workflows, Waku communication, deadlines, and gasless relay interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to use a wallet private key with unreviewed transaction code. <br>
Mitigation: Review the CLI, SDK, dependencies, contracts, and relay behavior before installation; use only a dedicated low-balance wallet and never a primary wallet key. <br>
Risk: On-chain work requests can move escrow, collateral, or relay-authorized funds if transaction details are wrong. <br>
Mitigation: Require manual confirmation for every transaction amount, token, request address, deadline, counterparty, and signed relay message. <br>
Risk: Continuous Waku chat monitoring can expose agents to external messages and accidental disclosure of secrets or deliverables. <br>
Mitigation: Start Waku watch only for requests intentionally created or accepted, stop it when finished, and avoid sharing secrets or private deliverables in chat. <br>


## Reference(s): <br>
- [CHEESE ClawHub Skill Page](https://clawhub.ai/locjonz/skills/cheese) <br>
- [Etherscan L1 Token](https://etherscan.io/address/0x68734f4585a737d23170eea4d8ae7d1ced15b5a3) <br>
- [Basescan V4 Factory](https://basescan.org/address/0x74fAc2A0E4526c8636978782F77c519C35091b61) <br>
- [Basescan Rewards](https://basescan.org/address/0xadd7c2d46d8e678458e7335539bfd68612bca620) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and TypeScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve on-chain transaction, wallet, relay, and Waku chat workflows that require human confirmation.] <br>

## Skill Version(s): <br>
4.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
