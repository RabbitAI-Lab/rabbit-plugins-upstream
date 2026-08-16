## Description:

Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability from camera footage, without wearable devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze local or remote face video for non-contact vital-sign estimates, structured health-reference reports, and cloud-hosted history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face/video health data to a vendor cloud service for analysis.

Mitigation: Use only with a clear privacy notice and explicit consent for health-video upload and cloud processing.

Risk: The skill silently creates or reuses an internal identity and keeps local token or profile records.

Mitigation: Provide a way to inspect or delete local identity data before deployment.

Risk: The skill can retrieve cloud history reports tied to the internal identity.

Mitigation: Disclose history lookup behavior and limit use to contexts where users expect cloud report retrieval.

Risk: The security verdict is suspicious because user-facing disclosure is weak for identity, storage, and cloud history behavior.

Mitigation: Review the skill before installation and install only where the privacy and consent model is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis output, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include progress messages, vital-sign analysis results, risk or recommendation text, report links, and Markdown tables for history results.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
