## Description:

从 Coding Agent 会话记录中提取交付证据，并对照规格清单审查需求覆盖情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to audit a completed development task by comparing its requirements with session evidence, then report coverage, gaps, and concrete follow-up checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit reports may expose private paths or metadata from the selected session or repository.

Mitigation: Select only the relevant session and repository, then review paths and metadata before sharing the report.

Risk: Partial evidence, inferred writes, or command counts may be mistaken for proof of requirement coverage or passing tests.

Mitigation: Treat these as clues; corroborate changes with git status, diff, or show and inspect actual test results or CI before judging coverage.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)
- [CodeSpecWeave paper](https://arxiv.org/abs/2610.40256)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown audit report with a requirements coverage matrix, evidence summary, and recommended checks; optional JSON evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence counts are clues and do not by themselves prove coverage or successful tests.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
