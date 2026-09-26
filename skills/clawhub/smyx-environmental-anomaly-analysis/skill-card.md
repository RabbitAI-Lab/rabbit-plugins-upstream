## Description:

Analyzes livestock barn video with environmental sensor data to identify behavior-linked stress responses caused by abnormal in-barn conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators, farm managers, and agent developers use this skill to analyze barn images, video, and optional sensor time series for behavior-environment anomaly reports and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the skill as suspicious because it sends barn media, sensor data, identity-linked history reports, and cached service tokens to a LifeEmergence/SMYX cloud service.

Mitigation: Install only where that service is trusted with the relevant farm media, sensor data, report history, and token handling.

Risk: The security evidence calls out silent identity creation/login, hidden identity override, and local token persistence as requiring human review.

Mitigation: Review or gate identity and token behavior before use in multi-user, farm-tenant, or sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON structured analysis output, including report links and tabular historical report results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a remote SMYX/LifeEmergence analysis service and return cloud report links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
