## Description:

Analyzes submitted videos of window and balcony areas for child climbing or leaning behavior and returns a structured risk report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, childcare centers, and system integrators can submit videos of window or balcony areas to review for child climbing, leaning, or related fall-risk behavior. Use results as an aid to supervision, not as a dependable real-time alarm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy controls may not protect private footage, and credential handling is unsafe.

Mitigation: Wait for fixes to destination override, export-only mode, and credential handling before providing private footage or API secrets; confirm provider retention, account isolation, and billing terms.

Risk: The workflow does not establish dependable immediate child-safety alarms.

Mitigation: Treat results as submitted-video analysis and continue adult supervision; do not rely on this skill for real-time alarms.

## Reference(s):

- [API reference](references/api_doc.md)
- [Analysis API details](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured analysis results and report links; report listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes submitted video or image inputs; reports are an aid to supervision and do not provide dependable real-time alarms.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
