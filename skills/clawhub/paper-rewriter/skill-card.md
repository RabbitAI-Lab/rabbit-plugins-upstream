## Description:

A bilingual Chinese-English toolkit for reviewing academic writing style, cleaning mechanical artifacts, guiding revisions, and checking that key facts and terminology remain intact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and academic authors use it to review Chinese- or English-language manuscripts for natural style and clearer prose while checking that numbers, citations, and terminology remain intact. Its style reports are heuristic self-checks, not AI detection, and the toolkit does not support concealing AI use or misrepresenting authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated checks do not establish factual correctness or guarantee that every document detail survived revision.

Mitigation: Keep the original and write revisions to a separate explicit path; manually compare numbers, citations, and terminology, and review warnings even after a verification pass.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Project repository (linked in README)](https://github.com/docsor1212/paper-rewriter)
- [English style guide](references/style_guide_en.md)
- [Chinese style guide](references/style_guide_zh.md)
- [Honest boundaries](references/honest_boundaries.md)
- [Permissions](references/permissions.md)
- [Compliance guidance](references/compliance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, CSV, DOCX]

**Output Format:** [Revised manuscript text or DOCX, with Markdown, JSON, HTML, or CSV reports and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local processing using Python's standard library; PDF reading is experimental, and DOCX write-back preserves plain paragraphs rather than complex layouts.]

## Skill Version(s):

4.4.0 (source: server release evidence and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
