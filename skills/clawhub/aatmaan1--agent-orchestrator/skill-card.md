## Description: <br>
Meta-agent skill for orchestrating complex tasks through autonomous sub-agents by decomposing work, generating specialized agent instructions, coordinating file-based communication, and consolidating results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aatmaan1](https://clawhub.ai/user/aatmaan1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to break complex work into parallelizable subtasks, create specialized sub-agent workspaces, coordinate inbox/outbox communication, monitor status, and consolidate deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sub-agents may receive broad file, shell, and execution authority without enough built-in limits or approval checkpoints. <br>
Mitigation: Before use, set explicit limits for the number of agents, accessible paths, file edits, shell commands, and approval requirements. <br>
Risk: Parallel autonomous agents can produce conflicting, incomplete, or low-quality deliverables if progress is only checked at completion. <br>
Mitigation: Use measurable success criteria, review status.json checkpoints, validate each outbox deliverable, and require human review before consolidation. <br>
Risk: Generated workspaces may retain sensitive inputs, intermediate files, or stale outputs after the workflow finishes. <br>
Mitigation: Define workspace archive and deletion rules before dispatch, then clean or archive temporary agent workspaces after consolidation. <br>


## Reference(s): <br>
- [File-Based Communication Protocol](references/communication-protocol.md) <br>
- [Sub-Agent Templates](references/sub-agent-templates.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/aatmaan1/skills/agent-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, JSON status examples, and generated SKILL.md templates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces task decomposition plans, sub-agent role definitions, file-based coordination structures, status tracking conventions, and consolidation summaries.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
