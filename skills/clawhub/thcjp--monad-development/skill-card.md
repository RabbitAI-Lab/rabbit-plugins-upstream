## Description: <br>
Helps developers build Monad dapps by producing code, configuration, shell commands, and troubleshooting guidance for Solidity contracts, Foundry deployment, frontend setup, and contract verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to scaffold, configure, deploy, test, and verify Solidity smart contracts and Monad dapp frontends. It is intended for technical blockchain development workflows, not broad non-technical tasks or decisions requiring independent human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deployment commands may broadcast blockchain transactions or use private keys. <br>
Mitigation: Require explicit confirmation before running commands with --broadcast or private keys, use test wallets, and pass secrets through environment variables. <br>
Risk: Contract verification may upload contract source, constructor arguments, and build metadata to an external verification service. <br>
Mitigation: Submit verification data only after confirming that sharing those artifacts with agents.devnads.com is acceptable. <br>


## Reference(s): <br>
- [Monad testnet RPC endpoint](https://testnet-rpc.monad.xyz) <br>
- [Devnads contract verification API](https://agents.devnads.com/v1/verify) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with code blocks, command snippets, configuration examples, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain deployment and verification commands that require manual review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact SKILL.md frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
