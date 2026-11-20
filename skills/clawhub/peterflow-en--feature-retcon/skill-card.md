## Description:

Reconcile a changed decision across an in-flight feature, with stage checks, a reversible file journal and independent closure evidence. Resume partial rounds or undo one on explicit request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT

## Use Case:

Developers and project teams use this skill to reconcile a changed decision across in-flight work, track the authorized stages, and preserve recovery and closure evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restoration may overwrite or delete recorded changes, and the security assessment reports concerns about tool scope and environment access.

Mitigation: Use restore only for an explicit undo request; review the affected paths and preserve a separate copy of current work before restoring, then verify the resulting files.

## Reference(s):

- [Feature Retcon on ClawHub](https://clawhub.ai/peterflow-en/skills/feature-retcon)
- [Impact assessment guide](references/assessment.md)
- [Contract and recovery protocol](references/contract-schema.md)
- [Stage gates](references/stage-gates.md)
- [Closure evidence](references/closure-evidence.md)
- [Contract tool](scripts/contract.py)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown plans and reconciliation records, JSON evidence, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stage assessments, file journal instructions, verification results, and recovery guidance.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
