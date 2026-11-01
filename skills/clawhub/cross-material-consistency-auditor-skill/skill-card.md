## Description:

Compares two or more materials on the same topic to identify inconsistencies and recommend unified wording without changing originals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, communications teams, and editors can compare press releases, articles, slide decks, web pages, white papers, and social posts before publication. The skill flags factual and wording drift, proposes source-grounded unified wording, and leaves changes to human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying proposed wording without review could introduce inaccurate or misleading guidance.

Mitigation: Review the reference source and each recommendation; keep changes under human control.

Risk: Audit reports may contain sensitive details from the compared materials.

Mitigation: Write reports to a separate output location and restrict access when they contain sensitive information.

Risk: The skill definition's version field is malformed and may prevent loading.

Mitigation: Correct the version field before loading; the server-resolved release version is 1.0.7.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill)
- [Consistency checklist](references/consistency-checklist.md)
- [Replay references](references/replay-references.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [JSON and Markdown, including extracted claims, a diff matrix, an audit report, and unified-wording recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves original materials; recommendations require human confirmation.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
