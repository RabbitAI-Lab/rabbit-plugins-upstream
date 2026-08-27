## Description:

Gunakan saat user minta reasoning mendalam sebelum bertindak pada task kompleks berdependensi banyak.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this meta-skill to structure complex or high-risk work with deeper reasoning, decomposition, hypothesis testing, tool selection, anti-hallucination checks, and completion verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broad and can influence complex or high-risk tasks.

Mitigation: Apply it only when its trigger conditions fit the task, and use its confirmation, dry-run, and verification gates before destructive or high-impact actions.

Risk: Ancillary README and backup content are more expansive than the active skill definition.

Mitigation: Review the active SKILL.md before deployment and clean or reconcile bundled support files when publishing updates.

Risk: Reasoning guidance can still lead to incorrect or misleading proposals if accepted without review.

Mitigation: Review and scan the skill before deployment, then verify important claims against observable evidence during use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/brain-core-ultra)
- [README](README.md)
- [Skill Definition](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text, with code blocks or shell commands when the user's task requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only reasoning guidance; concrete outputs depend on the user's task and the host agent's tools.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and SKILL.md metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
