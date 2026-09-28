## Description:

Helps authors self-check academic writing for possible AI-generated passages, review style and terminology, and prepare clearer writing and disclosure guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and editors use this local tool to review academic drafts for writing quality, terminology consistency, possible AI-generated passages, and AI-assistance labeling before submission. Its scores are self-review aids, not institutional determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-writing scores may be unreliable for short passages, English text, medical prose, or mixed human/AI drafts.

Mitigation: Treat scores as self-review signals, check the reported limitations, and inspect passages rather than using scores as submission or misconduct verdicts.

Risk: Auto-fix and reference-refresh operations can change local files or detector data.

Mitigation: Review batch and auto-fix output before accepting edits, and back up local reference data before refreshing it.

Risk: Polishing guidance could be misused to obscure AI assistance.

Mitigation: Use it to improve original writing and follow institutional AI-use and disclosure requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](artifact/references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML reports, Guidance]

**Output Format:** [Text or JSON self-checks and polishing guidance; optional HTML paragraph report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local batch reviews; optional supervised model is not bundled.]

## Skill Version(s):

4.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
