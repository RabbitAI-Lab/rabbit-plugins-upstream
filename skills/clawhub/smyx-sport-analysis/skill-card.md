## Description:

Analyzes outdoor sports event images or videos for participant injury, distress, posture, environmental, and other safety risks, then returns structured risk reports and warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External event organizers, medical support teams, and developers use this skill to submit outdoor sports event media for cloud-based safety risk analysis and to retrieve structured reports or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive participant videos, URLs, report metadata, and internally resolved identity data may be sent to the LifeEmergence cloud service.

Mitigation: Use only with appropriate consent, access controls, and privacy and retention review; avoid sensitive production footage until the publisher adds explicit disclosures.

Risk: The skill may silently create or reuse persistent identity records and store tokens.

Mitigation: Review account and credential handling before deployment, restrict where the skill can run, and rotate or remove stored credentials when no longer needed.

Risk: Automatic historical-report triggers may retrieve cloud report lists without a separate confirmation step.

Mitigation: Gate history-report workflows with user confirmation and authorization checks in environments that contain private reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown reports and JSON result data, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, abnormal behavior records, trend analysis, recommendations, history tables, and cloud report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
