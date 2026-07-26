## Description: <br>
Cryptographic identity for AI agents that can register on-chain identities, sign messages, verify other agents, link platform accounts, and stake USDC to support identity and vouching workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rosepuppy](https://clawhub.ai/user/rosepuppy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to create or import an agent identity key, register an on-chain identity, sign and verify messages, link platform accounts, look up identities, and vouch for other agents with USDC. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores identity private keys as local plaintext key material. <br>
Mitigation: Use a fresh low-value key, do not import a main wallet private key, restrict file permissions, and review the generated key file location before use. <br>
Risk: Registration, linking, and vouching commands can submit blockchain transactions and stake USDC. <br>
Mitigation: Verify the registry address, network, USDC amount, and target identity before execution, and require explicit user approval for transaction-producing commands. <br>
Risk: JSON-mode command flows may reduce interactive confirmation around transaction-producing actions. <br>
Mitigation: Treat JSON command output as data only and add a separate human or policy approval step before running register, link, or vouch operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rosepuppy/skills/agent-identity) <br>
- [Project homepage](https://github.com/g1itchbot8888-del/agent-identity) <br>
- [Publisher profile](https://clawhub.ai/user/rosepuppy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create local key material, read blockchain state, and submit transactions when executed by the user or agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
