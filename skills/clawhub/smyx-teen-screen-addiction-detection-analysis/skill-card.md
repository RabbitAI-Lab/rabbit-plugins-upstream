## Description:

Analyzes fixed-camera images or videos of adolescents to estimate head-down screen-use posture, screen-time duration, alert level, and family-facing reminders without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and family-health application developers use this skill to analyze home, study-room, or classroom camera footage for adolescent screen-use posture, cumulative screen-looking time, and gentle intervention reminders. It is intended for behavioral reporting and caregiver guidance, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes children's camera footage and identity-linked report history through a cloud service.

Mitigation: Use only with documented guardian and youth consent, clear retention and deletion practices, controlled access to reports, and appropriate limits on where cameras are used.

Risk: Evidence security summary reports hidden identity setup, local token storage, history access, and insecure default HTTP endpoints.

Mitigation: Confirm HTTPS-only transport, token handling, account separation, and history access controls before installation or deployment.

Risk: Screen-use classification can be mistaken for normal study behaviors or treated as a diagnosis.

Mitigation: Review outputs as behavioral signals only, exclude reading, writing, and online classes when appropriate, and avoid medical or punitive conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON analysis, report links, history lists, and reminder guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the rendered analysis text to a user-specified output file.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
