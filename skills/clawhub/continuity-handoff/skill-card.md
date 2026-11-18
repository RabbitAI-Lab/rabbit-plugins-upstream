## Description:

Create a compact fresh-task continuity packet that preserves goals, decisions, proof, protected state, and a bounded read-only handle to legacy Codex history. Use when replacing a bloated or legacy task without forking its transcript, handing work to a fresh task, or retrieving one missing historical fact without loading the full conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theangrypit](https://clawhub.ai/user/theangrypit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to hand accepted work to a fresh task without carrying over a large legacy transcript. It creates a durable Markdown packet and, when a fact is missing, retrieves a bounded, read-only history window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scan coverage is partial, so the benign verdict has medium confidence.

Mitigation: Review the components that were not fully inspected and decide whether the remaining uncertainty is acceptable before installing.

Risk: A bounded history recall can include sensitive text from a legacy task.

Mitigation: Keep recall question-specific, never search history for credentials, and avoid copying sensitive text into packets or onward.

## Reference(s):

- [Continuity packet template](references/packet-template.md)
- [Continuity Handoff on ClawHub](https://clawhub.ai/theangrypit/skills/continuity-handoff)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files]

**Output Format:** [Markdown continuity packet and concise text evidence capsule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact and task-specific; historical recall is question-driven, read-only, and bounded.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
