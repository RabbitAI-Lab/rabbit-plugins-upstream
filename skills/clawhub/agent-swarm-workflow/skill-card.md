## Description: <br>
Agent Swarm Workflow is Jeffrey Emanuel's multi-agent implementation workflow for coordinating NTM, Agent Mail, Beads, and BV during the execution phase after planning and bead creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdnw](https://clawhub.ai/user/clawdnw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering leads use this skill to run supervised parallel implementation workflows with multiple coding agents, coordinate work through Beads and Agent Mail, and keep agents moving through review and commit loops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow gives coding agents broad authority to edit, commit, and push code. <br>
Mitigation: Use a dedicated branch or worktree and require human review before any commit or push. <br>
Risk: A misconfigured Agent Mail, NTM, or BV setup can lead to poor coordination or conflicting edits. <br>
Mitigation: Verify the coordination tools before starting and monitor file reservations, task status, and agent messages during the run. <br>
Risk: Secrets or sensitive project details could be exposed through project files or agent messages. <br>
Mitigation: Keep secrets out of project files and agent communications; use approved secret stores or environment configuration instead. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/clawdnw/skills/agent-swarm-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code] <br>
**Output Format:** [Markdown with prompt text, shell commands, and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human supervision before applying, committing, or pushing agent-produced changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
