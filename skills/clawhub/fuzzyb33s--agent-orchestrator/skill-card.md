## Description:

Meta-agent skill for orchestrating complex tasks through autonomous sub-agents by decomposing macro tasks, coordinating file-based handoffs, and consolidating results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to break complex work into parallel sub-agent tasks, coordinate file-based communication, and consolidate agent outputs into final deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous sub-agent delegation can run broad task plans with limited control gates.

Mitigation: Review the planned agents, task boundaries, workspace paths, tool access, input files, and expected outputs before dispatch.

Risk: Use on sensitive repositories or private data can expose information to generated sub-agent workflows.

Mitigation: Avoid sensitive inputs unless explicit confirmation, scoping controls, and output review are in place.

Risk: Broad automatic triggers may activate the skill when a user only intended ordinary task discussion.

Mitigation: Confirm that macro-task delegation is intentional before using the orchestrator.

## Reference(s):

- [Agent Orchestrator on ClawHub](https://clawhub.ai/fuzzyb33s/skills/agent-orchestrator)
- [File-Based Communication Protocol](references/communication-protocol.md)
- [Sub-Agent Templates](references/sub-agent-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, file specifications, and JSON status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces orchestration plans, sub-agent skill templates, workspace instructions, status conventions, and consolidation guidance.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
