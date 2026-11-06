## Description:

Detects image quality issues in camera footage, including black or white screens, color casts, stripes, noise, and blurriness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Security and camera operations teams can submit images or video for quality checks and receive issue classifications, clarity scores, recommendations, and links to reports. They can also query prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted footage is sent to configured LifeEmergence services, whose retention and deletion terms were not verified.

Mitigation: Confirm the destination service and its retention and deletion terms before submitting sensitive footage.

Risk: The --export-env-only option does not prevent uploads, and --api-url may not redirect processing as expected.

Mitigation: Do not rely on these options to control data transfer; have the service and network behavior reviewed before use with sensitive footage.

Risk: Automatic account setup handles credentials without adequate user control, including identity reuse and token storage concerns.

Mitigation: Request fixes to account setup, identity reuse, and token storage before using sensitive credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured image quality analysis reports with findings, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query and display historical reports]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
