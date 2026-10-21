## Description:

Scans authorized PikPak folders for possible advertising or promotional files, reports candidates by confidence, and only prints cleanup commands for individually approved items from a frozen report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can scan a specifically authorized folder for likely bundled advertisements, promotional material, or junk and review a confidence-tiered report. They can approve individual items from a frozen report to print cleanup commands; the skill does not execute deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filename-based candidate rules can misclassify files, and manually running a cleanup command may cause unrecoverable data loss.

Mitigation: Use a trusted PikPak CLI and scan only the authorized folder; keep reports private, review each candidate, and verify recovery behavior before manually running any printed command.

## Reference(s):

- [PikPak Ad Cleaner release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON scan report and text summary; optional printed PikPak cleanup commands]

**Output Parameters:** [An authorized folder ID for scanning; optional frozen report, report SHA-256, and explicitly approved item IDs for command generation]

**Other Properties Related to Output:** [Read-only scanning; cleanup commands are printed only after explicit approval and are never executed automatically.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
