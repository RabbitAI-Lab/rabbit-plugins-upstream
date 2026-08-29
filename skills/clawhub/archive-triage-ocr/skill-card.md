## Description:

Helps agents classify paper receipts and app screenshots, decide what to archive or ignore, run OCR, and maintain searchable timeline indexes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adchina2025](https://clawhub.ai/user/adchina2025)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, archivists, and personal knowledge management users use this skill to triage personal document archives, generate searchable OCR sidecar Markdown, and maintain timeline indexes while avoiding unnecessary screenshot retention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal financial or document archives can contain sensitive information.

Mitigation: Use local OCR when possible, review any cloud OCR use before sending data, and keep archive access limited to the intended directories.

Risk: OCR or triage decisions can misclassify documents or retain unnecessary screenshots.

Mitigation: Use the skill's temporary holding area and regular human review process before final archive, ledger, or deletion decisions.

Risk: Generated OCR sidecar files or indexes can become incorrect or stale.

Mitigation: Run read-back verification after batch processing and refresh timeline indexes after manual frontmatter corrections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adchina2025/skills/archive-triage-ocr)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with OCR sidecar and timeline index conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local OCR workflows, archive triage decisions, frontmatter fields, and review routines.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
