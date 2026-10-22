## Description:

Analyzes home-arrival camera footage for fatigue signals and offers gentle after-work care suggestions and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Residents and smart-home developers can analyze the first 30 minutes of after-work camera footage for fatigue indicators, receive gentle care suggestions, and review past reports. The results are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home camera footage, video URLs, and fatigue history may be sent to a cloud service.

Mitigation: Confirm informed opt-in and bystander notice; review retention and deletion before sharing footage.

Risk: Account identity may be set up without prompting, and tokens may persist.

Mitigation: Review account identity and token storage, and verify pause and disable options before use.

Risk: Fatigue scores may be mistaken for medical diagnoses.

Mitigation: Treat findings as non-diagnostic care guidance and seek a qualified professional for health concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Fatigue analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured fatigue analysis with care suggestions and report links; historical reports as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the analysis result to a file.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
