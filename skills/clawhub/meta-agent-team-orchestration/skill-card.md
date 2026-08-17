## Description:

Provides meta-agent orchestration guidance distilled from an agent-team workflow, with claimed self-verification, reflection, and learner-loop enhancements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to structure multi-agent work around task creation, role assignment, review, verification, and follow-up reporting. It is best treated as orchestration guidance plus a lightweight local learner log rather than as a verified autonomous safety framework.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact claims self-verification, rollback, and self-evolution behavior that the authoritative security evidence says is not actually implemented.

Mitigation: Treat the skill as orchestration guidance and require independent tests, reviews, or verified safety controls before using it for sensitive work.

Risk: The bundled learner records local state, which may persist notes from prior use.

Mitigation: Review learner output before sharing artifacts and avoid recording secrets, personal data, or sensitive operational details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/meta-agent-team-orchestration)
- [Publisher Profile](https://clawhub.ai/user/qq435912743)
- [Distillation Report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with optional code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record local learner state when the bundled learner script is invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
