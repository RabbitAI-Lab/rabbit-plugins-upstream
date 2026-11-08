## Description:

Analyzes surveillance images and video by comparing faces with a known-person database and produces stranger-recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security and site-management teams use the skill to review authorized surveillance images or video, compare detected faces with a known-person database, and receive recognition reports and alerts. It can also retrieve prior reports and enroll a person in the reference database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive surveillance media and identity data and sends material for remote processing; cloud history and reference-database changes are also reported concerns.

Mitigation: Process only media and identity records you are authorized to use, and confirm the service's data handling and retention practices before sending them.

Risk: Some options may trigger analysis unexpectedly, and enrollment or history actions may affect account or reference data.

Mitigation: Run analysis or history lookup only when explicitly requested, and confirm before enrolling a face or changing reference data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Alerts]

**Output Format:** [Structured recognition reports in JSON or readable text, with report links and history listings when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include known-person and stranger counts, similarity results, warnings, recommendations, and links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
