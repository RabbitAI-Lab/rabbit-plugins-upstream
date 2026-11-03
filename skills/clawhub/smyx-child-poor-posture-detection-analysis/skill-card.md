## Description:

Submits a child's study video or video URL for cloud-based posture analysis and returns a structured report with estimated posture metrics and reminder text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to submit a child's study video for posture analysis or retrieve previously generated reports. Results are visual estimates and reminder text, not medical diagnoses; the supplied package does not provide continuous camera monitoring or spoken alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review is needed because a broken no-analysis option can still upload children's videos, while cloud account creation and saved login credentials lack clear user controls.

Mitigation: Do not rely on --export-env-only to prevent processing or uploads. Before using children's footage, confirm guardian consent covers transfer to Lifeemergence and review account creation, retention and deletion terms, local credential storage, and possible charges.

Risk: The supplied package does not implement continuous camera monitoring or spoken alerts.

Mitigation: Treat it as a tool for submitted-video analysis and text reports; do not rely on it for ongoing monitoring or audible reminders.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [API documentation](references/api_doc.md)
- [Product demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Files]

**Output Format:** [Structured analysis report and status text; report output can be saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report content depends on the cloud analysis service and may include estimated posture metrics, reminder text, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
