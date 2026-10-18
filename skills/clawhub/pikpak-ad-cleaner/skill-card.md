## Description:

Scans authorized PikPak folders for suspected promotional files, produces a tiered report, and prints removal commands only for individually approved items without executing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can review suspected ads in an explicitly authorized folder before deciding whether to remove any files. The skill reports candidates and can print commands for individually approved IDs but does not delete files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning an authenticated cloud account can expose private file names and paths in reports.

Mitigation: Confirm the exact authorized folder ID before scanning and keep reports in a private directory.

Risk: Filename-based classifications can be wrong, and the recoverability of printed removal commands has not been verified.

Mitigation: Inspect each candidate, approve IDs individually, and do not run printed removal commands unless their effect and recoverability have been independently confirmed.

Risk: Unrelated affiliate onboarding may steer users toward a referral code.

Mitigation: Ignore the affiliate registration path unless you intentionally choose to use that referral code.

## Reference(s):

- [PikPak Ad Cleaner on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)
- [Upstream design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Plain-text findings, JSON reports, and optional printed shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports group candidates as high, review, and protected; commands are printed only for approved IDs from a complete, checksum-bound report and are never executed.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
