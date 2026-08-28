## Description:

Based on computer vision, this skill analyzes workplace images or videos to detect employee phone use during work hours, summarize frequency and duration, and return monitoring results and efficiency guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise operations teams and workplace management agents use this skill to analyze authorized office monitoring images or videos for phone-use events, report counts and duration, and retrieve prior cloud-hosted monitoring reports. Use should be limited to environments with lawful authority, employee notice, and appropriate privacy controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace surveillance analysis may process employee images, video, and behavioral inferences without adequate notice or authority.

Mitigation: Use only with lawful authority, employee notice or consent, and documented privacy controls for collection, retention, access, and review.

Risk: The scanner reports silent identity creation or reuse and local token storage.

Mitigation: Review account provisioning and token storage before installation, and require explicit consent or administrative approval for identity creation and history lookup.

Risk: The scanner reports media and identifiers are sent to under-disclosed cloud or development endpoints.

Mitigation: Verify endpoint ownership, transport security, deployment environment, and retention policy before sending production or employee data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Phone Usage Monitoring API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include detected phone-use counts, duration statistics, compliance scores, warnings, improvement suggestions, and links to cloud-hosted reports.]

## Skill Version(s):

1.0.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
