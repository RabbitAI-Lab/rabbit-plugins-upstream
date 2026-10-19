## Description:

Scans authorized PikPak folders for suspected promotional files, produces a graded review report, and prints cleanup command suggestions only after explicit approval without executing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and administrators can review suspected advertisements and promotional files in folders they have authorized for scanning. They can inspect candidates before approving any suggested cleanup commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote filenames may be unsafe when displayed in a terminal.

Mitigation: Prefer the JSON report over terminal rendering when filenames may be untrusted.

Risk: Reports may expose private PikPak paths.

Mitigation: Limit scans to authorized folders and store reports in a private directory.

Risk: Registration guidance includes a referral code that may reward the publisher.

Mitigation: Use the referral code only if you intentionally choose to; review the skill before installing.

Risk: Suggested cleanup commands could target files misclassified as promotional or have unverified recovery behavior.

Mitigation: Verify the PikPak CLI executable, review every suggested command manually, and confirm recovery behavior before acting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)
- [Upstream design notes](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands]

**Output Format:** [Graded text or JSON scan report; optional printed shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports classify high, review, and protected items; commands require approval of individual IDs and are never executed by the skill.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
