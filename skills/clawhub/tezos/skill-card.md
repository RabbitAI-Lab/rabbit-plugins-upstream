## Description: <br>
Expert Tezos blockchain development guidance for security-first smart contract development, FA1.2 and FA2 token standards, gas optimization, testing, and production deployment patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[efekucuk](https://clawhub.ai/user/efekucuk) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and smart contract engineers use this skill when building, reviewing, optimizing, testing, or deploying Tezos L1 smart contracts and FA1.2/FA2 token implementations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deployment or transfer examples can create irreversible on-chain state or spend real XTZ when run against mainnet. <br>
Mitigation: Before approving octez-client commands, confirm the target network, account, contract address, transfer amount, burn cap, and dry-run status; approve mainnet commands only when real spending and permanent state changes are intended. <br>
Risk: Smart contract guidance can be misapplied to high-value contracts without sufficient validation. <br>
Mitigation: Run comprehensive Shadownet testing and require security review before mainnet deployment, especially for contracts holding user funds or privileged controls. <br>


## Reference(s): <br>
- [Tezos Skill on ClawHub](https://clawhub.ai/efekucuk/skills/tezos) <br>
- [Tezos Docs](https://docs.tezos.com) <br>
- [LIGO Documentation](https://ligolang.org) <br>
- [OpenTezos](https://opentezos.com) <br>
- [TzKT Explorer](https://tzkt.io) <br>
- [Tezos Improvement Proposals](https://gitlab.com/tezos/tzip) <br>
- [Tezos Testnet Registry](https://teztnets.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with LIGO, Michelson, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose ligo and octez-client commands for contract compilation, testing, simulation, and deployment.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
