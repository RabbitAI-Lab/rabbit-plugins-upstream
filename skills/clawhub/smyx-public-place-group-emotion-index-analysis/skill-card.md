## Description:

Analyzes footage from fixed cameras in public venues to estimate aggregate facial-expression distributions and a group emotion index, with operational suggestions and safety alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Venue operators and analysts use the skill to review public-space footage and receive aggregate emotion summaries by area, alongside service-improvement suggestions and safety alerts. Results are operational aids, not assessments of individual people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports video uploads and account or credential handling; scan coverage is partial.

Mitigation: Before deployment, confirm where footage and identity or token data are sent or stored, who can access them, and how long they are retained.

Risk: Analysis may run when an operator intends only to export settings.

Mitigation: Confirm that export-only actions do not start an analysis job, and review the selected action and footage before execution.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Recommendations, Alerts]

**Output Format:** [Structured JSON reports, with Markdown summaries and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aggregate emotion distributions, group and regional indices, trends, and operational or safety suggestions.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
