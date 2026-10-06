## Description:

Helps scholars revise Chinese and English academic prose with local style checks, mechanical cleanup, and safeguards for citations, numbers, and terminology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and editors use this skill to identify formulaic phrasing, improve the clarity of their own academic drafts, and check that revisions preserve facts and required AI-use disclosures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch and report runs may write to unintended output paths.

Mitigation: Review input and output paths before running batch processing or producing reports.

Risk: Writing improvements could be misused to conceal AI assistance or misrepresent authorship.

Mitigation: Use the skill for legitimate editing and comply with institutional or publisher AI-use disclosure requirements.

Risk: An automatically drafted term list may omit terminology that must remain unchanged.

Mitigation: Review and complete generated terms before relying on the integrity check.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Best practices](artifact/references/best_practices.md)
- [Academic integrity and disclosure guidance](artifact/references/compliance.md)
- [English style guide](artifact/references/style_guide_en.md)
- [Chinese style guide](artifact/references/style_guide_zh.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Plain text, Markdown, JSON, HTML, and CSV reports; revised text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, user-directed outputs; style scores are heuristic self-checks, not authorship determinations.]

## Skill Version(s):

2.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
