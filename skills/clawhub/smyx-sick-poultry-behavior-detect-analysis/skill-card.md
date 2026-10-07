## Description:

Analyzes poultry and pig barn images or videos for signs of abnormal behavior and returns risk-ranked findings and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and animal-health teams use this skill to screen barn footage for abnormal poultry or pig behavior and review risk levels and historical reports. Findings support early triage, not veterinary diagnosis or treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn images, videos, and report metadata are sent to a cloud service.

Mitigation: Use non-sensitive media and confirm that the service and its data handling are acceptable before running an analysis.

Risk: The skill can silently create or reuse an account identity and store tokens in workspace data.

Mitigation: Review local credential storage and restrict workspace access before use.

Risk: Historical report queries use a cloud identity with limited user-facing control.

Mitigation: Confirm the publisher-service relationship and the reports accessible to that identity before querying history.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior types, affected locations, risk levels, and report links; results are screening aids, not diagnoses.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
