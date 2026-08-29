## Description:

Detects climbing, playing with fire, touching power sources, and dangerous actions near windows, providing real-time alerts for child safety supervision in homes, kindergartens, and nurseries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to submit child-monitoring media for hazardous-behavior recognition, alerts, structured reports, and report history lookup in home, kindergarten, or nursery settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real child, home, school, or nursery footage may be uploaded or referenced by URL for backend analysis.

Mitigation: Use only approved media with appropriate consent, and install the skill only after trusting the publisher and backend data flow.

Risk: The skill can silently create or reuse an internal identity and store service tokens in the local workspace database.

Mitigation: Run it in an isolated workspace, restrict local file access, and clear local identity or token state when the analysis session is complete.

Risk: Cloud report history queries can expose sensitive child-monitoring reports.

Mitigation: Limit history access to authorized users and review report history behavior before enabling the skill in shared environments.

Risk: Automated alerts are an auxiliary child-safety aid and may miss or misclassify dangerous behavior.

Mitigation: Require human confirmation of alerts and do not use the skill as the sole supervision or emergency-response mechanism.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include detected behavior details, alert status, recommendations, report links, and cloud report history results.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter and auto changelog mention 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
