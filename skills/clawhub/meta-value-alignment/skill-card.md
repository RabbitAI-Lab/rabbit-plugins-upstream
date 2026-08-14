## Description:

Meta Value Alignment is a distilled value-alignment meta-skill that adds self-verification, reflection, super-agent orchestration, and continuous learning loops to value-alignment tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to apply value-alignment checks with added self-verification, reflection, and learning-memory support during agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cross-session notes and user preferences may retain sensitive or project-specific information.

Mitigation: Avoid recording secrets or personal data in learner notes, and clear learned_patterns.json between users or sensitive projects.

Risk: Self-modification guidance could weaken controls or introduce incorrect alignment behavior if accepted without review.

Mitigation: Review proposed skill changes and scan the skill before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/meta-value-alignment)
- [Distillation Report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local learned-pattern notes when the learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
