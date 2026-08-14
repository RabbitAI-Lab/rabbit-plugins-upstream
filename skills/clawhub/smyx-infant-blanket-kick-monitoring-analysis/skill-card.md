## Description:

Identifies babies kicking off blankets or exposing their bodies during sleep and alerts parents to cover them up to prevent catching a cold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and agents assisting with nursery monitoring use this skill to analyze infant sleep video or image inputs for blanket-kicking, body exposure, and related alert/report output. It can also retrieve cloud-hosted historical monitoring reports associated with the current workspace identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant sleep footage and report queries are sent to LifeEmergence cloud endpoints.

Mitigation: Use only with explicit caregiver approval, approved media handling policy, and inputs that are appropriate to transmit to the configured cloud service.

Risk: The skill can silently create or reuse a local workspace identity and associate cloud report history with that identity.

Mitigation: Review identity behavior before deployment and require confirmation before historical report retrieval in environments with privacy or consent requirements.

Risk: A local workspace database can store service tokens used by the skill.

Mitigation: Limit file permissions for the workspace, rotate tokens after testing, and prefer a version with explicit token retention and deletion controls.

Risk: Monitoring output is an auxiliary signal and may be wrong or incomplete.

Mitigation: Do not use the output as a substitute for caregiver supervision, safe sleep practices, or other infant safety monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant blanket monitoring API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include monitoring results, recommendations, report links, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
