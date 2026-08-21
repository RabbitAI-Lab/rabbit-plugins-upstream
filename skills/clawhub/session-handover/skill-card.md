## Description:

Shift-style continuity notes with ownership, limits, hazards, protected targets, receipts, and exact next action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create compact continuity notes when pausing work, changing the lead model, or preparing a fresh model to continue safely. It focuses the handover on current state, ownership, protected targets, limits, hazards, receipts, and the exact next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated handover notes may include secrets, personal data, or irrelevant private material from session history.

Mitigation: Review and redact generated notes before keeping or sharing them.

Risk: A handover can carry stale decisions, overbroad copied context, or uncertain state into the next session.

Mitigation: Verify volatile claims against current workspace state and keep hazards, protected targets, limits, and receipts explicit.

Risk: Missing ownership or resource-limit details can cause duplicated work, unsafe continuation, or exhausted budgets.

Mitigation: Mark unknown ownership and limits as unknown rather than implied safe, and require the next agent to verify them before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pinguy/skills/session-handover)
- [Publisher profile](https://clawhub.ai/user/pinguy)
- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/session-handover)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown handover note with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for durable session notes such as SESSION_NOTES.md, daily memory entries, or active typed blackboards.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
