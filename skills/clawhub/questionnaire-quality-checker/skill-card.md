## Description:

Screens CSV questionnaire data for missingness, invalid or out-of-range values, within-scale straightlining, and extreme-response patterns, then produces respondent-level flags for manual review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yunyue619](https://clawhub.ai/user/yunyue619)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and data-quality reviewers use this skill to configure transparent screening rules for psychological questionnaire CSV data and summarize cases that need manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quality flags may be mistaken for automatic exclusion decisions.

Mitigation: Review flagged respondents manually and apply pre-defined study rules before excluding any data.

Risk: Incorrect scale ranges or thresholds in the JSON configuration can produce misleading screening results.

Mitigation: Review the configuration against the questionnaire codebook before running the checker.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and JSON quality reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags cases for review; does not automatically delete responses.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
