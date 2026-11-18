## Description:

A bilingual Chinese and English toolkit for academic writing that flags templated phrasing, cleans mechanical artifacts, and guides clearer revision with checks for numbers, citations, and terminology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars, including non-native English writers, use it to review and revise academic drafts for clearer, more natural prose and to check for style patterns or mechanical residue. Authors can inspect suggested changes and run integrity checks before adopting edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious because optional terminology rewriting may alter protected text and identifiers, and safeguards and documentation have reported weaknesses; scanner coverage was incomplete.

Mitigation: Review proposed rewrites manually and run verify.py against the original, with a terms file for domain terminology, before accepting edits; follow the skill's AI disclosure and academic-integrity guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Project repository](https://github.com/docsor1212/paper-rewriter)
- [ModelScope skill listing](https://modelscope.cn/skills/Docsor/paper-rewriter)
- [Compliance guidance](artifact/references/compliance.md)
- [Honest boundaries](artifact/references/honest_boundaries.md)
- [Integrity verification API](artifact/references/api.md)
- [English style guide](artifact/references/style_guide_en.md)
- [Chinese style guide](artifact/references/style_guide_zh.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Revised academic prose and Markdown reports or revision plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include style-pattern findings and integrity-check results; review proposed edits before adopting them.]

## Skill Version(s):

5.14.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
