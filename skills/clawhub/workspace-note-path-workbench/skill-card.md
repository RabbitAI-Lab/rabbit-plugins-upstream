## Description:

Write a workspace export file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge-base publishers and workspace users create a local CSV export from a supplied archive path and receive its recorded path and an effect receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send data to an external HTTP or SMTP destination after local file creation.

Mitigation: Review delivery environment variables and any delivery-config file; omit delivery settings when only a local export is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/workspace-note-path-workbench)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files]

**Output Format:** [JSON recorded_path and receipts; local CSV export file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes beneath the selected output directory; configured delivery may contact an external destination.]

## Skill Version(s):

1.1.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
