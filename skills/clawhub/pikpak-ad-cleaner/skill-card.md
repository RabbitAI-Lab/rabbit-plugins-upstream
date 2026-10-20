## Description:

Scans PikPak folder metadata for likely advertising and promotional files, reports candidates by confidence, and does not delete files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External PikPak users can inspect a folder or shared resource package for likely advertising, promotional, or junk files before deciding what to do. The report separates high-confidence, review, and protected items; cleanup commands require explicit approval and are never run automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no folder is specified, scanning defaults to the account root.

Mitigation: Specify the authorized folder explicitly before scanning.

Risk: Candidate classification can include false positives, and reports may contain private file information.

Mitigation: Keep reports private and review every candidate before approving cleanup.

Risk: Live PikPak CLI compatibility and cleanup recoverability are unverified.

Mitigation: Use a trusted CLI, verify compatibility and recoverability, and separately approve any execution of printed commands.

## Reference(s):

- [PikPak Ad Cleaner on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON scan report and human-readable text summary; optional cleanup commands as shell text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports classify candidates as high, review, or protected. Cleanup commands are only printed for individually approved entries in a frozen report and are never executed by the skill.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
