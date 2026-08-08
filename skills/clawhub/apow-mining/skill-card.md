## Description: <br>
This skill teaches your agent how to mine $AGENT coin via the apow-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentoshi](https://clawhub.ai/user/agentoshi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to set up a fresh encrypted APoW wallet, complete a Base funding handoff, and run the pinned Easy Mode miner after explicit approval. The workflow is limited to policy-capped APoW mining with a fresh low-balance hot wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow mines with real assets on Base and can spend funds within local policy caps. <br>
Mitigation: Use a fresh low-balance wallet, require explicit approval before running, and verify the CLI-displayed policy caps before proceeding. <br>
Risk: Wallet secrets or keystore passwords could be exposed if handled through chat or project files. <br>
Mitigation: Never request, read, reveal, copy, or transmit wallet secrets; users must enter keystore passwords directly in their local terminal or secret manager. <br>
Risk: Running an alternate or unpinned package version could change mining behavior or policy enforcement. <br>
Mitigation: Invoke only the pinned Easy Mode command and stop if the package version, contract addresses, chain, approval scope, or policy state differs from what the CLI displays. <br>


## Reference(s): <br>
- [ClawHub APoW Mining skill page](https://clawhub.ai/agentoshi/skills/apow-mining) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash command and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before invoking the pinned Easy Mode command.] <br>

## Skill Version(s): <br>
0.12.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
