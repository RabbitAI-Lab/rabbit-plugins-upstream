## Description:

Analyzes workplace camera footage against individual baselines to produce employee emotion-fluctuation alerts and HR support reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams and authorized managers use this skill to review trends in workplace camera footage and receive alerts and supportive check-in suggestions for employees. Reports are intended for internal care, not employment decisions or medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-risk workplace camera monitoring can expose sensitive employee behavior and undermine consent.

Mitigation: Obtain legal, HR, security, and employee-representative review before installation; enforce informed consent and opt-out outside the skill.

Risk: Cloud reports and persistent identity handling can expose employee data or enable unauthorized access.

Mitigation: Enforce role-based access, audit logging, retention limits, and token cleanup outside the skill.

Risk: Emotion alerts can be misleading or misused in employment decisions.

Mitigation: Treat alerts as non-diagnostic prompts for voluntary support and never use them for performance, promotion, or termination decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON reports, Guidance]

**Output Format:** [Structured analysis reports and Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes emotion-trend alerts, baseline comparisons, and suggested HR support actions; can list cloud-hosted historical reports.]

## Skill Version(s):

1.0.11 (source: server-resolved release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
