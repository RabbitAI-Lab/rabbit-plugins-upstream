## Description:

Helps academic authors review AI-writing signals, terminology and style consistency, and disclosure labels, with sentence-level revision guidance and local reports for text or Word drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Academic authors use this skill to self-check manuscripts for AI-writing signals, inconsistent terminology, writing conventions, and disclosure labels before revising or submitting their work. It offers findings and revision advice rather than rewriting the manuscript or providing an institutional detection verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manuscripts may contain sensitive or unpublished material.

Mitigation: Point the skill only at manuscripts or directories you intend it to read, and review generated reports before sharing them.

Risk: AI-writing scores may be mistaken for definitive institutional findings.

Mitigation: Treat scores as self-review guidance, verify flagged passages yourself, and follow your institution's disclosure policy.

Risk: Automatic terminology normalization or optional model setup can write local files.

Mitigation: Review proposed edits before accepting them; use --auto-fix only when normalized output is wanted, and provide only trusted model files to optional setup.

## Reference(s):

- [Paper Polisher Pro release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Project documentation site](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown, JSON, HTML, CSV]

**Output Format:** [Human-readable analysis and revision suggestions; optional Markdown, JSON, HTML, and CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are generated locally; AI-risk scores are advisory, and text under 100 characters receives no risk verdict.]

## Skill Version(s):

5.5.0 (source: release metadata, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
