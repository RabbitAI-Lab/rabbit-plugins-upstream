## Description:

A distilled academic translation meta-skill that adds self-verification, self-reflection, super-agent orchestration, and continuous learning loops to an academic translation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to translate academic materials while preserving formulas, citations, tables, terminology, and bilingual review outputs. It also records self-checks and learning feedback to improve future translation runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may keep local learning state about prior uses or user preferences.

Mitigation: Use an explicit opt-in learning file with inspect and delete controls, or disable the learner behavior before deployment.

Risk: The skill describes self-modification of its own instructions after repeated failures or usage.

Mitigation: Forbid writes to SKILL.md in production and require human review for any proposed instruction changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-academic-translation)
- [Publisher profile](https://clawhub.ai/user/qq435912743)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured translation artifacts with inline shell commands and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create translation-output folders, self-check notes, bilingual HTML, and local learning state when the learner behavior is enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
