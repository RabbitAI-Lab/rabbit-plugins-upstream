## Description:

Analyzes videos to evaluate human eating behaviors, habits, and dietary patterns, identifies tendencies toward unhealthy eating, and provides structured analysis reports with nutritional improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and health-focused agents use this skill to submit meal videos or video URLs for dietary behavior analysis, structured reporting, and nutritional improvement guidance. Agents can also retrieve cloud-hosted historical diet-analysis reports for the current internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads meal videos or video URLs to the LifeEmergence/SMYX backend for analysis.

Mitigation: Use it only with media appropriate for that backend and confirm the configured endpoint is a production HTTPS service before running analysis.

Risk: The skill automatically creates or reuses a local identity record and can retrieve prior diet-analysis reports.

Mitigation: Confirm that local identity and workspace data handling matches the deployment policy, and trigger history lookup only when prior reports are intended to be retrieved.

Risk: Dietary behavior results may be mistaken for medical or nutrition diagnosis.

Mitigation: Present results as health guidance only and direct users to qualified medical or nutrition professionals for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON reports with analysis results, risk notes, recommendations, report links, and optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; history lookup is returned from the cloud API.]

## Skill Version(s):

1.0.13 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
