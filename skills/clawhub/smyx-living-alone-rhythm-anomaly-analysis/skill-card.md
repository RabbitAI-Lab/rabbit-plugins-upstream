## Description:

Analyzes night-time fixed-camera home video to detect lights-off timing and early-morning activity, compare those observations with a personal baseline, and produce sleep-rhythm anomaly reminders without making medical diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, family-support workflows, and developers building remote-care automations can use this skill to analyze night-time camera inputs for changes in sleep rhythm and early-morning movement. Results are intended as visual activity and routine-deviation signals for follow-up, not as clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Night-time home video and derived behavioral reports are highly sensitive personal data.

Mitigation: Use only with explicit informed consent from the monitored person or an authorized guardian, and confirm retention, access, sharing, and deletion practices before deployment.

Risk: Cloud processing may expose video, report data, and alert workflows to vendor-side handling.

Mitigation: Deploy only where the organization accepts the vendor cloud data flow, and limit who can view reports or receive family/community alerts.

Risk: Reusable identity tokens or default identities can make report association persistent across sessions.

Mitigation: Confirm how tokens and default identities are created, stored, rotated, and removed before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lights-off timing, early-morning motion counts, baseline comparisons, anomaly labels, alert text, and historical report links.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
