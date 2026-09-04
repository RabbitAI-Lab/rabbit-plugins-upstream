## Description:

plan-it generates self-contained interactive HTML plan files with embedded JSON state, session catchup, SHA-256 attestation, IDE mirroring, templates, and Markdown or JSON export for multi-step agent work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use plan-it to turn complex tasks into persistent, navigable planning artifacts instead of transient chat-only plans. It is intended for workflows that need interactive phases, task state, evidence notes, approvals, and exportable planning records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill auto-runs local hooks while plan.html exists.

Mitigation: Review hook behavior before installing and disable or remove hooks in environments where automatic local execution is not acceptable.

Risk: The skill reads local agent session metadata for session catchup.

Mitigation: Use it only in workspaces where that local metadata access is acceptable and avoid installing it in shared or highly sensitive environments.

Risk: HTML plan files may contain embedded plan data that should not be trusted when received from another source.

Mitigation: Open and share plan.html only when the embedded plan data is trusted, and review exported content before acting on it.

Risk: SHA-256 attestation is tamper-evident, not proof of authorship or safety.

Mitigation: Treat the badge as a change indicator, re-attest only at deliberate review points, and do not rely on it as a guarantee.

## Reference(s):

- [Server-resolved source repository](https://github.com/OthmanAdi/plan-it/tree/main/skills/plan-it)
- [Markdown predecessor](https://github.com/OthmanAdi/planning-with-files)
- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/plan-it)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local HTML, JSON, and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single self-contained plan.html as the canonical planning artifact, with optional Markdown and JSON exports.]

## Skill Version(s):

0.1.0 (source: release metadata; skill metadata reports 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
