## Description:

Analyzes a child's classroom or home study video for visual signs of drowsiness and returns a fatigue estimate and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and teachers can use the skill to review a child's study video for visual signs of drowsiness, receive a fatigue estimate, and decide whether to adjust the activity or suggest a rest. It is a learning aid, not a medical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still upload children's videos, so sensitive footage may be sent for remote processing.

Mitigation: Avoid sensitive footage until the option is fixed; confirm the video processing path and obtain guardian authorization before use.

Risk: Remote account creation and readable access-token storage leave control over accounts, credentials, and stored reports unclear.

Mitigation: Confirm account creation and deletion behavior, determine how recordings and reports can be deleted, use HTTPS production settings, and protect the workspace database containing tokens.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured fatigue assessment and report links in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a 0–100 fatigue score, fatigue level, drowsiness events, and rest reminders; results are visual estimates, not medical diagnoses.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
