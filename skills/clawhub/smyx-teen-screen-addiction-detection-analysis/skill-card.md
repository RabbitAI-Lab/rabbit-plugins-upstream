## Description:

Analyzes camera footage of teens for screen-use posture and duration, then provides screen-time summaries and gentle reminders when configured thresholds are exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and authorized caregivers use the skill to review teen screen-use estimates from camera footage and receive gentle reminders and daily summaries. It also supports retrieving previous reports from a cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera footage of minors is sent to cloud APIs for analysis.

Mitigation: Require explicit consent from both guardian and teen; confirm cloud endpoints, access controls, retention, and deletion terms before use.

Risk: Monitoring in private or school settings may expose sensitive behavior and identities.

Mitigation: Avoid bedrooms and school deployments without a clear privacy and deletion process; restrict access to footage and reports.

Risk: The skill may silently create or reuse identities and store service tokens and profile data locally.

Mitigation: Treat the local workspace database as sensitive, limit access, and review identity and token storage before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports, Markdown report tables, and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screen-use duration estimates, posture classifications, alerts, gentle recommendations, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release; bundled SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
