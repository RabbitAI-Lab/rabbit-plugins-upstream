## Description:

This skill analyzes in-cabin driver face images or video for visual signs of facial flushing and sweat glare, then returns structured alerts and suggested actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, fleet operators, and vehicle safety teams use this skill to analyze driver-facing DMS media for visual flushing and sweating abnormalities. The output supports assistive alerts and fleet reporting, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive driver face and health-related data while using persistent identities and report history.

Mitigation: Require explicit consent for biometric processing and history access, document what video, identity, and report data is uploaded or stored, and apply appropriate privacy controls before deployment.

Risk: Security evidence flags dev/plaintext HTTP defaults, stored tokens, and incomplete dependency declarations.

Mitigation: Remove dev/plaintext HTTP defaults, use secure token storage, and fix dependency declarations before installation or production use.

Risk: Visual flushing and sweat detection can be affected by lighting, vehicle window tinting, occlusion, and individual differences.

Mitigation: Treat outputs as assistive, non-diagnostic alerts and combine them with baseline comparison, duration thresholds, and appropriate human or medical follow-up.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-flushing-sweat-detection-analysis)
- [Driver flushing and sweat detection API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-oriented text from command-line/API analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual abnormality metrics, health-risk reminders, recommended actions, and report links; outputs are not medical diagnoses.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
