## Description:

Analyzes driver face video from an in-cabin DMS camera to report eye open/closed state, blink rate, eye-closure duration, microsleep indicators, and fatigue warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and fleet safety teams use this skill to analyze driver face videos or video URLs for blink-rate, eye-closure, PERCLOS, and fatigue-warning reports. It is intended as an auxiliary safety signal, not a medical diagnosis or a substitute for driver judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver face video or video URLs may be sent to external services and linked to persistent local or remote identity state.

Mitigation: Obtain driver consent, verify the service operator, retention policy, and deletion process, and use only approved media sources.

Risk: Fatigue warnings may be unreliable when the driver's eyes are obscured, lighting is poor, glare is severe, or the video does not meet the documented frame-rate and visibility requirements.

Mitigation: Use compliant DMS camera footage with stable eye visibility and treat results as auxiliary safety guidance requiring human judgment.

Risk: The security evidence reports a suspicious verdict because the skill handles remote media and persistent account or token state.

Mitigation: Review service endpoints, account and token handling, and deployment controls before installation.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and JSON-style structured analysis from shell or API execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue metrics, warning types, recommended actions, report links, or a saved output file path.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
