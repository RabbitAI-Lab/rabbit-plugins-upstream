## Description:

Turns CSV files into short, plain-English briefs grounded in locally computed profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[goofproof](https://clawhub.ai/user/goofproof)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing spreadsheet exports use this skill to summarize each CSV's profiled counts, numeric values, missing data, and questions worth investigating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated profile and brief may expose text values and aggregate numbers from a CSV when shared.

Mitigation: Profile only CSVs suitable for local analysis and review outputs before sharing them outside your environment.

## Reference(s):

- [CSV Brief homepage](https://ronin.md/skills/csv-brief/)
- [CSV Brief on ClawHub](https://clawhub.ai/goofproof/skills/csv-brief)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Plain-English Markdown brief and JSON profile]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One brief per CSV; the profile includes column statistics and may include sample text values.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
