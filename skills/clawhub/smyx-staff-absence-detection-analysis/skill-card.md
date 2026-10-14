## Description:

Analyzes workplace images and videos for staff absence and provides monitoring reports and cloud-hosted report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized workplace supervisors use this skill to assess staffing at monitored posts from images or videos, review absence alerts and reports, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace images and videos are uploaded to a third-party cloud service.

Mitigation: Use only with authorization to process employee media; review consent, retention, and service access controls before use.

Risk: The skill can silently create or reuse persistent identities and store login tokens locally.

Mitigation: Restrict access to the workspace and local credential store; review account creation and token retention before deployment.

Risk: Cloud-hosted historical reports may expose employee monitoring records.

Mitigation: Limit report access to authorized personnel and verify retention and access controls with the service provider.

## Reference(s):

- [Staff absence monitoring API documentation](artifact/references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Structured analysis text or JSON, with Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and save results to a local file.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md states 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
