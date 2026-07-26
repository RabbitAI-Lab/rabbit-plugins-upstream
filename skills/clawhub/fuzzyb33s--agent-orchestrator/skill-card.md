## Description: <br>
Meta-agent skill for orchestrating complex tasks through autonomous sub-agents by decomposing tasks, generating sub-agent workspaces, coordinating file-based communication, and consolidating results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to break complex work into parallel subtasks, dispatch specialized sub-agents, track file-based handoffs, and consolidate deliverables. It is intended for deliberate orchestration workflows where workspace changes, generated files, and cleanup actions are reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill coordinates sub-agents that may create, copy, archive, or clean up workspace files. <br>
Mitigation: Confirm the target workspace, expected file changes, copied inputs, and cleanup or archive actions before running an orchestration workflow. <br>
Risk: Task decomposition and sub-agent outputs can introduce incorrect, incomplete, or conflicting guidance into final deliverables. <br>
Mitigation: Review agent instructions, status files, outbox deliverables, and the consolidated result before using or deploying the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fuzzyb33s/agent-orchestrator) <br>
- [File-Based Communication Protocol](references/communication-protocol.md) <br>
- [Sub-Agent Templates](references/sub-agent-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, file specifications, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces task breakdowns, generated agent instructions, workspace file layouts, status tracking guidance, and consolidation summaries.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
