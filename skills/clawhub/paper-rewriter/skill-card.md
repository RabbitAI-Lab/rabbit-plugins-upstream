## Description:

Helps scholars review and revise Chinese and English academic prose with style checks, mechanical cleanup, and checks that preserve factual details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and editors use this skill to identify formulaic phrasing, revise academic drafts for clarity, and check that numbers, citations, and terminology remain intact. Its style scores are self-review aids, not proof of authorship or AI use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic cleanup or rewriting could alter a manuscript's meaning or miss errors in extracted PDF text.

Mitigation: Review edits and extraction-confidence warnings against the original manuscript, then run the integrity check before use.

Risk: Style cleanup could be mistaken for evidence of human authorship or used to omit required AI-use disclosures.

Mitigation: Treat scores as self-review guidance only and keep any required AI-use disclosures separate from editing.

Risk: Learned term exceptions persist locally and may affect later style checks.

Mitigation: Review and remove unneeded learned guards before subsequent scans.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Best practices](artifact/references/best_practices.md)
- [English style guide](artifact/references/style_guide_en.md)
- [Chinese style guide](artifact/references/style_guide_zh.md)
- [Academic integrity and disclosure](artifact/references/compliance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Revised prose and style, revision, and integrity reports in text, Markdown, HTML, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local files and optional change-tracking reports; review edits before submission.]

## Skill Version(s):

2.8.0 (source: ClawHub release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
