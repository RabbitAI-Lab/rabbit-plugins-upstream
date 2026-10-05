## Description:

Assembles reproducible exam papers from a local question bank and blueprint, and checks existing papers for coverage, scoring, difficulty, and time-budget gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and assessment teams use the skill to select questions from their own bank against an exam blueprint, review gaps in a proposed paper, and gate checks in CI. The skill does not create question text or replace final human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing to a custom or global target writes persistent skill files and may clean existing yotta-item residue there.

Mitigation: Review the target directory before using --dir or -g, and use a pinned npm version or reviewed release tag when reproducibility matters.

Risk: Bank difficulty labels and automated checks do not establish a paper's educational suitability.

Mitigation: Have the assessment team review question content and the finished paper before use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-item)
- [Project homepage (listed in release metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-item)
- [Question bank format](references/bank-format.md)
- [Exam blueprint format](references/blueprint-format.md)
- [Report format and findings](references/report-format.md)
- [Privacy and content boundaries](references/privacy.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON exam-assembly and checking reports; JSON starter templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fixed seeds reproduce question selection; findings identify missing or mismatched requirements. Papers reference question IDs rather than reproducing question text.]

## Skill Version(s):

0.1.1 (source: server release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
