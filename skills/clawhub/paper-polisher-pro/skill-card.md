## Description:

Helps academic authors review Chinese and English drafts for possible AI-generated patterns, writing quality, terminology, and AI-use labeling, with local reports and revision guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this skill to self-review drafts, check terminology and AI-use labeling, and get actionable polishing guidance before submission. Detection scores are advisory, not proof of authorship or substitutes for institutional checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recursive batch review can inspect unintended draft files.

Mitigation: Choose the input directory deliberately and enable --batch --recursive only when all supported files beneath it should be reviewed.

Risk: Applying fixes or refreshing reference data can change local files.

Mitigation: Run --apply or freshness_refresh.py only when you intend those local changes; keep a copy of important drafts and reference data.

Risk: Polishing or de-AI guidance could be misused to conceal AI assistance.

Mitigation: Use it for self-review and quality improvement, and disclose AI assistance according to institutional policies; do not misrepresent authorship.

Risk: Detection scores can be misleading for short texts, mixed authorship, medical prose, English, or newer models.

Mitigation: Treat scores as advisory, heed no-verdict and degraded-mode notices, and verify concerns through human review rather than using scores as proof.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](references/article-review-workflow.md)
- [Publisher documentation](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, JSON reports, HTML reports, CSV summaries]

**Output Format:** [Markdown guidance and commands; optional local JSON, HTML, and CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual Chinese and English; texts under 100 characters receive no risk verdict; optional local supervised model is not bundled.]

## Skill Version(s):

4.3.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
