## Description:

A distilled self-alignment skill that checks candidate text against machine-readable constitutional rules, conservatively revises violations, and reports an audit trace with an alignment verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to review and revise generated text against constitutional-style policy rules, then inspect the resulting alignment score, edits, and final ALIGNED or UNALIGNED verdict. It is also positioned as a meta-skill for self-verification and reflection workflows, but those claims should be reviewed against the actual local scripts before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learner notes may store user preferences, task details, or error patterns from sensitive work.

Mitigation: Run the learner only with explicit consent and define redaction, deletion, and storage controls before use.

Risk: The artifact suggests automatic SKILL.md write-back while also describing a read-only safety boundary.

Mitigation: Disable or review any self-modification workflow and require human approval for changes to the skill definition.

Risk: Claims about reason-verification, reflection loops, and super-agent orchestration are broader than the included local scripts demonstrate.

Mitigation: Treat those capabilities as claims requiring integration review and validate actual dependencies before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-constitutional-self-alignment)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance and JSON audit output from local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The alignment checker emits revised text, final violation counts, an alignment score, a verdict, iteration traces, and a human-review flag.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
