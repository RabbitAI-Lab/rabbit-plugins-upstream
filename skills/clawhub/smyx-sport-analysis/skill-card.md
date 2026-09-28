## Description:

Analyzes outdoor sports footage for potential injuries and health risks, then provides structured reports, warnings, and safety guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and safety teams use the skill to review outdoor sports footage for possible falls, injuries, or signs of distress and to retrieve past analysis reports. Its findings support, but do not replace, professional medical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Participant footage or URLs, potentially containing health-related information, are sent to lifeemergence.com services.

Mitigation: Obtain appropriate consent and avoid uploading sensitive footage unless the service's data handling is acceptable.

Risk: The skill silently creates or reuses an account identity and stores access tokens in the workspace.

Mitigation: Use an isolated workspace; review local-data deletion and token-revocation procedures before use.

Risk: Cloud report history may contain sensitive participant information.

Mitigation: Limit access to report history and avoid sharing report links with unauthorized recipients.

Risk: Video-based safety findings may be mistaken for a medical diagnosis.

Mitigation: Treat findings as advisory and seek professional medical help for suspected injuries or emergencies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Sports analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis reports and JSON results; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk warnings and report links; results can optionally be saved to a file.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
