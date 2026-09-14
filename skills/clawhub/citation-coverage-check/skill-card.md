## Description:

Scans sentences containing numbers, dates, or claims, measures the share with source markers, and returns a gap list when citation coverage falls below the configured threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, editors, and governance reviewers use this skill to check draft reports or generated text for citation coverage before publication or handoff. It helps identify numeric or date-bearing claims that lack visible source markers, but it does not replace expert, legal, regulatory, or domain review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable global install instructions can fetch changing upstream code into an agent skill directory.

Mitigation: Install from a reviewed commit or release, avoid global installation unless the source is trusted, and do not use elevated privileges.

Risk: The checker can miss unsupported citation styles or produce incomplete coverage judgments.

Mitigation: Treat the report as an auxiliary review signal and have a qualified reviewer confirm important claims and sources.

Risk: Important operating guidance is mostly Chinese, which can lead to misuse by readers who cannot review it fully.

Mitigation: Have non-Chinese users review translated documentation before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/citation-coverage-check)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON reports with exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports claim count, covered claim count, coverage ratio, threshold, pass/fail status, and uncovered sentence snippets.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
