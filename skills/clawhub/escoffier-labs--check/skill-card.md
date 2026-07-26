## Description: <br>
Prompts agents to verify claims of completion, fixes, test passes, or subagent success with fresh evidence before reporting them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[escoffier-labs](https://clawhub.ai/user/escoffier-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to make agents inspect current verification evidence before making success or completion claims. It is useful when an agent needs to report test, build, script, git status, or subagent outcomes accurately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Verification commands may have side effects or reveal sensitive local output if selected or quoted carelessly. <br>
Mitigation: Review commands before execution and include only relevant, non-sensitive output in user-facing reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/escoffier-labs/check) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text] <br>
**Output Format:** [Markdown or plain text guidance with command and output excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include relevant command output when verifying a claim.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
