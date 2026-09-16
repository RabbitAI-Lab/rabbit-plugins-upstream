## Description:

Through fixed enclosure cameras, the skill analyzes reptile behavior videos to detect movement frequency, dwell duration, activity rhythms, and basking-versus-hiding zone use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, and developers use this skill to analyze fixed-camera enclosure videos, generate thermal-zone utilization reports, and surface behavior-based reminders when activity patterns appear abnormal. The skill is intended for welfare and environment-optimization support, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags automatic account linkage and unsafe handling of enclosure videos, credentials, and historical reports.

Mitigation: Install only after confirming that users accept vendor-cloud processing under the automatically managed identity and that credential-bearing requests are limited to trusted hosts.

Risk: Development HTTP configuration and shared workspace token storage can expose video, report, or credential data.

Mitigation: Require HTTPS production endpoints, remove development HTTP settings before deployment, and avoid storing reusable tokens in a shared workspace database.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report with thermal-zone metrics, activity labels, alert level, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid disease diagnosis, medication names, dosing, and unauthorized device-control actions.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
