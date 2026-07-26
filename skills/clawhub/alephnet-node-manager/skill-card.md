## Description: <br>
Alephnet Node Manager helps teams manage AI agent social-network nodes, including distributed memory fields, multi-agent team orchestration, consensus validation, token-economy workflows, content storage, and identity signing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and enterprise teams use this skill to plan and execute Alephnet node workflows for shared memory management, multi-agent team orchestration, network coherence checks, wallet operations, and node configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet sends and staking commands can move or lock tokens. <br>
Mitigation: Require explicit user approval before wallet.send, wallet.stake, wallet.unstake, or related economic actions. <br>
Risk: Shared or global memory sync can expose secrets, personal data, or regulated business content. <br>
Mitigation: Review data before syncing and avoid organization or global scopes for sensitive material. <br>
Risk: Credential setup examples may lead users to store real API keys in plaintext. <br>
Mitigation: Use locked-down file permissions or a secrets manager, and do not place production keys in broadly readable files. <br>
Risk: Exec-driven package installation and node commands can alter the local environment or external services. <br>
Mitigation: Use an agent that asks for approval before package installation, exec commands, memory sync, and agent or team activation. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/alephnet-node-manager) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured JSON results and command proposals for Alephnet node operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
