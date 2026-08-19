## Description:

A meta reflection and replanning skill distilled from reflection-replanner that adds self-verification, self-reflection, super-agent orchestration, and a stateful learner loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to analyze failed plans, replan with verification steps, and record operational patterns for later reflection. It is intended for advanced reflection and replanning workflows where stateful learning is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to keep cross-session memory and remember usage history or preferences.

Mitigation: Install only where stateful memory is acceptable, avoid recording secrets or private task details, and review learner records before sharing or reuse.

Risk: The skill describes automatic edits to its own skill instructions after repeated errors or use.

Mitigation: Disable or gate automatic SKILL.md edits behind human review, source control review, and a separate approval process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-reflection-replanner)
- [SKILL.md](artifact/SKILL.md)
- [Distillation report](artifact/distillation_report.md)
- [Learner script](artifact/scripts/learner.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional learner records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local learner state when the learner workflow is used.]

## Skill Version(s):

1.0.0 (source: evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
