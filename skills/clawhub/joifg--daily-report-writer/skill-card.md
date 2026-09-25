## Description:

Generates a daily report Markdown draft from user-provided date, highlights, and optional blockers, then writes it under the reports directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joifg](https://clawhub.ai/user/joifg)

### License/Terms of Use:


## Use Case:

Employees and individual contributors use this skill to draft daily work reports from structured highlights and blockers. It is suited for routine status reporting where the agent should produce a local Markdown draft for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes a dated Markdown file under reports/, and overwrite behavior is not defined in detail.

Mitigation: Review the target file path before use when important files may already exist in the reports directory.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown file plus structured status, summary, data, and nextAction response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes reports/{{date}}-daily-report.md and returns missing-parameter or file-permission guidance on failure.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
