## Description:

Submits crib video for infant blanket-coverage and kicking analysis, then returns the analysis result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and baby-monitoring product teams can submit crib video to review blanket coverage and kicking events, and retrieve prior analysis reports. Treat results as auxiliary monitoring information; they do not replace adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that observed behavior may not match the infant-monitoring claims, so analysis and alerts may not behave as expected.

Mitigation: Review the release and verify its behavior before relying on analysis results or alerts.

Risk: Infant video, account identity data, and stored tokens may be involved, and video may be sent to a remote service.

Mitigation: Before installing, establish how video, account creation, identity data, and tokens are handled; obtain guardian consent and protect recordings.

Risk: The export-only option may still analyze video, and scanner coverage was partial because a referenced local path could not be resolved.

Mitigation: Do not rely on export-only mode to avoid analysis; review the complete release contents and understand video handling before execution.

Risk: The skill may not provide continuous monitoring or reliable alerts.

Mitigation: Maintain adult supervision and independently verify any alert or monitoring result.

## Reference(s):

- [API interface reference](artifact/references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results as JSON or text; history results can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blanket-coverage status, kicking events, alerts, and report links; results are auxiliary monitoring information.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
