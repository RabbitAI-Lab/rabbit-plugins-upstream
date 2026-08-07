## Description:

Detects hazardous child behaviors such as climbing, playing with fire, touching power sources, and risky window activity in monitoring media, then returns alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze child-monitoring video or image inputs for hazardous behavior indicators and to retrieve structured child-safety reports. It supports supervision workflows for homes, kindergartens, nurseries, and similar monitored spaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-monitoring videos or URLs are sent to a remote service for analysis.

Mitigation: Use only with appropriate consent and authorization, avoid uploading unnecessary sensitive content, and confirm remote processing is acceptable for the deployment context.

Risk: The skill may create or reuse an account identity, persist tokens locally, and retrieve cloud report history automatically.

Mitigation: Review account-linking behavior before deployment, restrict host access to local credentials, and clear or rotate stored credentials when no longer needed.

Risk: Cloud report history can be retrieved automatically with limited user-facing control.

Mitigation: Run the skill in a controlled environment, verify report-history access expectations with users or administrators, and monitor outbound service access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON analysis reports with optional report links and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hazard detections, risk summaries, recommendations, alert-threshold context, and cloud report links.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
