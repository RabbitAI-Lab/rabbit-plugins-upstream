## Description:

Analyzes pet toy-area videos or video URLs through cloud APIs to report toy interaction frequency, duration, preferences, daily activity curves, trend comparisons, and activity-decline alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet toy-area video files or public video URLs for descriptive interaction activity analysis. It can also query saved cloud history and return standardized report tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet videos or public video URLs to Life Emergence cloud APIs.

Mitigation: Use only when cloud processing of the submitted pet video content is acceptable.

Risk: The skill requires an open-id, username, or phone number for saved reports and cloud history.

Mitigation: Provide only an intended account identifier and review whether cloud history storage is appropriate before running analysis or history queries.

Risk: The security evidence reports possible remote account creation or use and local SQLite token retention.

Mitigation: Review credential-retention behavior before installation and remove local stored credentials when they are no longer needed.

Risk: Activity-decline alerts may be mistaken for medical or emotional diagnosis.

Mitigation: Treat outputs as descriptive behavior observations only and do not use them as diagnostic conclusions.

## Reference(s):

- [Pet Toy Interaction Activity Analysis API Documentation](artifact/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-toy-interaction-activity-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown reports and tables, JSON or text command output, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [History queries are formatted as Markdown tables with report links; analysis results are descriptive and not diagnostic.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
