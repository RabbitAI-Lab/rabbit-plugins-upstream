## Description:

Analyzes videos of aquarium animals and returns a structured report with observed features, possible health concerns, and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers use the skill to review video of fish and other aquatic pets for visible health concerns, possible disease signs, and care suggestions. It can also retrieve earlier analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags account and personal-data handling, credential storage, video transmission, and possible video upload even when export-only mode is selected.

Mitigation: Review the service and credential handling before use, avoid sensitive footage, and do not rely on export-only mode to prevent upload.

Risk: Broad history-query triggers may retrieve earlier reports when the user did not intend a lookup.

Mitigation: Confirm that a history lookup is intended before retrieving or sharing prior reports.

Risk: Automated visual findings may be incomplete or mistaken when used to assess an animal's health.

Mitigation: Treat the report as reference information and consult a qualified aquatic veterinarian for health decisions.

## Reference(s):

- [Skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Structured aquatic-pet health report with observations, possible concerns, and care suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prior-report listings or report links; findings are for reference and do not replace veterinary diagnosis.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
