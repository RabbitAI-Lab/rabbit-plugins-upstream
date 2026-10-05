## Description:

Helps academic authors review drafts for AI-writing signals, terminology, style, translation issues, and disclosure-labeling needs through local self-check reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this skill to self-review Chinese or English manuscripts, locate passages needing attention, and prepare clearer, more consistent writing with appropriate AI-use disclosure. Scores are advisory rather than institutional AI-detection verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected manuscripts and generated reports can contain sensitive or unpublished work.

Mitigation: Review the files and destinations you select; keep local reports and any corrected files under appropriate access controls.

Risk: Maintenance or setup actions can change local files or model installation.

Mitigation: Run setup and apply-mode freshness or recalibration commands deliberately, separately from routine analysis.

Risk: De-AI and attack-evaluation capabilities could be misused to conceal AI assistance.

Mitigation: Use them for author self-review, not to evade detection; follow institutional AI-use and disclosure policies.

Risk: AI-writing scores can be misleading for short texts, medical prose without the optional model, English text, or mixed-authorship documents.

Mitigation: Treat scores as advisory, inspect paragraph-level evidence and degraded-mode notices, and do not substitute them for institutional assessments.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Project documentation](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Reports]

**Output Format:** [Markdown and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local per-document or batch scores, paragraph findings, and polishing suggestions; reports may be saved to user-selected files.]

## Skill Version(s):

4.6.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
