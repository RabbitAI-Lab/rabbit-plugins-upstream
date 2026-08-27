## Description:

Structured session lifecycle for Claude Code - start, checkpoint, end, and daily heartbeat commands that maintain project state across conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Claude Code users use this skill to carry project context across conversations by starting sessions with state briefings, checkpointing progress, closing sessions with logs and state updates, and running daily heartbeat reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes local project memory files and session logs, which may preserve sensitive context or incorrect summaries if accepted without review.

Mitigation: Review generated summaries before /end or /update writes, and keep generated state and session files only in projects where persistent local memory is intended.

Risk: Claude memory proposals can affect future project conversations if approved.

Mitigation: Approve Claude memory additions only when the information should be reused across future project conversations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/conorbronsdon/skills/cot-session-management)
- [Bundled README](artifact/README.md)
- [Bundled Skill Instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with short status briefings, inline shell commands, and local Markdown state/session records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes or proposes updates to local state and session Markdown files when the user invokes the lifecycle commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
