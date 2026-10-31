## Description:

Analyzes UAV imagery of farmland to calculate vegetation indices and produce a crop health map with reported low-health zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and agricultural service teams use the skill to review UAV orthomosaics or imagery, inspect vegetation-index results, and locate areas for field follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill silently manages accounts and saved login details, and its export-only option can still trigger uploads.

Mitigation: Wait until the export-only behavior and account controls are corrected. Before use, approve the service receiving imagery and clarify retention, account creation, and charges. Protect the workspace credential database, and do not rely on --api-url to change the destination.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Report links]

**Output Format:** [Structured analysis results with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes vegetation-index results and reported health zones; report lists are returned as structured data.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
