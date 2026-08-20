## Description:

Analyzes consented workplace camera video through remote services to produce anonymized employee emotion-fluctuation alerts and HR care reports based on facial-expression, posture, behavior, and 30-day baseline signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams and workplace administrators use this skill to analyze consented office-area video or query prior reports for anonymized emotion trend alerts and supportive-care recommendations. It is intended for voluntary HR care workflows, not medical diagnosis, performance management, promotion, or termination decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive workplace video and employee emotion indicators.

Mitigation: Use only with explicit employee consent, legal approval, opt-out handling, clear notice, and documented limits on retention and use.

Risk: Remote report access and backend endpoints may expose sensitive HR reports if authorization is misconfigured.

Mitigation: Verify backend endpoints, API authorization, report export access, and audit logging before deployment.

Risk: Local account, token, and database behavior may persist identifiers or access tokens.

Mitigation: Review local token storage, database permissions, rotation, and cleanup before running the skill with real employee data.

Risk: Emotion alerts could be misused as employment or medical determinations.

Mitigation: Restrict outputs to supportive HR care workflows and prohibit use for diagnosis, performance review, promotion, or termination decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured report text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include anonymized subject IDs, workstation IDs, baseline comparisons, alert levels, HR care suggestions, historical report lists, and export links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
