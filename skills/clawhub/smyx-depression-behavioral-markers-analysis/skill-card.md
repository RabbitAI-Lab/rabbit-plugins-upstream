## Description:

Analyzes home camera footage from bedroom and dining areas to summarize changes in time in bed and eating behavior and flag patterns that may warrant a check-in; it is an observational aid, not a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and community health workers can use the skill to review multi-day camera observations for changes in an older or solo-living person's bed time and eating activity, then decide whether to check in or seek professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private camera footage may be uploaded for analysis, including when an export-only option is selected.

Mitigation: Obtain the recorded person's informed consent before use, verify the export-only behavior, and confirm the service's video retention and deletion terms before sending footage.

Risk: On Windows, HTTP logging can expose sensitive requests.

Mitigation: Have the Windows logging behavior fixed before using private footage, and protect request logs and local credential data.

Risk: Behavior reports may expose a person's sensitive health-related observations or be mixed across users.

Mitigation: Use a dedicated account and workspace when reports need to remain separate, and restrict access to reports and credentials.

## Reference(s):

- [Skill listing](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured text or JSON behavior summary with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes bed-time and eating observations against a personal baseline; not a medical diagnosis.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
