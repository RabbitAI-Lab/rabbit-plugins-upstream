## Description:

Analyzes submitted video for adolescents’ screen-looking posture and duration, then returns a behavioral summary and reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized caregivers use the skill to review video for screen-looking posture and duration, and receive a summary with gentle reminders. The output describes observed behavior and is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account reuse can expose private reports.

Mitigation: Avoid shared-workspace use until account isolation is fixed.

Risk: Submitted footage may contain sensitive information about adolescents.

Mitigation: Obtain the required consent and confirm the service’s retention and deletion practices before submitting footage.

Risk: The export-env-only option does not prevent processing, and credentials may be written to destinations that are not suitable for sensitive use.

Mitigation: Do not treat that option as a no-processing mode; restrict credential destinations before sensitive use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured analysis text or JSON with a report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture observations, screen-use duration summaries, behavioral reminders, and historical report links.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
