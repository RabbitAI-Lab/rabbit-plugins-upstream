## Description:

Helps authors self-check AI-writing signals and improve academic drafts with style, terminology, translation, quality, and disclosure guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic authors use this local toolkit to review drafts for AI-writing signals, improve clarity and terminology, and check AI-use labeling before submission. Its scores are advisory, not institutional detection verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-detection feedback can be used to disguise AI-generated academic work.

Mitigation: Use for author self-review and quality improvement only; disclose AI assistance under institutional policies rather than attempting detector evasion.

Risk: Recursive batch processing can include sensitive drafts outside the intended set.

Mitigation: Select a narrow directory intentionally and avoid --recursive on broad private folders.

Risk: Maintenance commands with --apply can change package files.

Mitigation: Review intended changes before using --apply and retain a backup of package data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Reports]

**Output Format:** [Text, JSON, CSV, or HTML reports and polishing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-file and paragraph-level results; optional batch processing]

## Skill Version(s):

4.2.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
