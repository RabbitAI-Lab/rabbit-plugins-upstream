## Description:

This skill analyzes consented enterprise office camera video to compare anonymized facial-expression and posture signals with employee baselines and produce HR care alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR and authorized workplace wellbeing teams use this skill to analyze consented office video or URLs and generate anonymized emotion-fluctuation reports for voluntary care outreach. It should not be used for diagnosis, discipline, promotion, or termination decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive employee footage and workplace emotion signals.

Mitigation: Require legal, HR, security, and employee representative review before deployment, with explicit consent, opt-out controls, and documented limits on use.

Risk: Identity, network, and credential behavior needs careful review before real employee use.

Mitigation: Use approved camera and source allowlists, HTTPS-only production endpoints, no plaintext token storage, restricted HR access, retention limits, and complete audit logging.

Risk: Emotion-fluctuation outputs could be misused as employment or medical conclusions.

Mitigation: Limit outputs to voluntary care outreach and prohibit use for diagnosis, performance review, promotion, termination, or disciplinary decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown tables and JSON-style structured reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write report output to a requested file.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
