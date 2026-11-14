## Description:

Analyzes videos of outdoor sports events for possible injuries and health risks, then returns a structured report and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and safety teams use the skill to review participant video for possible falls, injuries, discomfort, posture concerns, and environmental hazards, and receive risk reports and first-aid suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags unclear remote account creation and data handling for uploaded video and reports.

Mitigation: Avoid installation until the publisher explains what data is sent, how accounts are created, and what consent or authorization is required; obtain appropriate consent before uploading participant footage.

Risk: The security evidence reports a mismatch between the stated sports-safety purpose and some observed behavior, and gaps between promised and observed capabilities.

Mitigation: Review the implementation and its data flows with the publisher before relying on it for event operations, and independently verify any high-risk alert.

Risk: The scan is incomplete because a referenced local path was missing.

Mitigation: Resolve the missing path and review the complete release before installation or use.

Risk: Visual analysis may mistake signs of injury or illness and could be mistaken for a medical diagnosis.

Mitigation: Treat results as preliminary safety indicators; stop activity and seek qualified medical help when someone appears unwell or injured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API details](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured JSON or a text report with risk findings, safety warnings, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, abnormal behavior records, and first-aid suggestions. Results are for safety reference and do not replace medical diagnosis.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
