## Description:

Daily Workflow preserves concise, evidence-backed project memory across start-work orientation, checkpoints, wrap-up, and handoff without overwriting governance or acceptance records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to resume work, save progress, record checkpoints, wrap up sessions, prepare handoffs, and reconcile stale workflow notes while preserving project governance boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow notes may accidentally retain sensitive project context if users ask the agent to persist too much detail.

Mitigation: Review generated notes before sharing and avoid recording secrets, credentials, private customer records, large logs, or confidential source bodies.

Risk: Project memory can become misleading if it overwrites governance records or treats unverified work as accepted.

Mitigation: Use read-only orientation first, preserve existing authority, keep verification and acceptance separate, and record blockers or unexecuted checks explicitly.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and project-local workflow note updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update scoped project memory files such as Docs/STATUS.md, Docs/NEXT_ACTIONS.md, or handoff notes when persistence is authorized.]

## Skill Version(s):

4.0.0 (source: server release metadata, SKILL.md, SECURITY.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
