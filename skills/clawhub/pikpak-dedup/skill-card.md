## Description:

Analyzes PikPak media folders for possible duplicate or alternate-version files and provides reviewable candidates without deleting anything.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and administrators review possible duplicate or alternate-version media files in an explicitly selected folder before deciding whether to remove any files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Name-based matches can group distinct media versions and do not prove identical content.

Mitigation: Review each candidate's details and verify content independently before approving an ID.

Risk: Running a printed pikpak rm command can remove files; recovery behavior is not verified.

Mitigation: Check the complete frozen report and its SHA-256 digest, approve IDs individually, and manually verify every ID before running any command.

Risk: Using the disclosed referral code may benefit its sharer.

Mitigation: Decline the referral code if you do not want to provide referral credit.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-dedup)
- [Upstream design and limitations](references/upstream-design.md)
- [Czkawka duplicate-checking guidance (technical background, not release provenance)](https://github.com/qarmin/czkawka/blob/eb8b91dbb4d25dff416202674ee0de84ee4b5e5c/instructions/Instruction_Core.md#L37-L47)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Human-readable analysis or JSON report; optional printed commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidates are not confirmed content duplicates; deletion commands are printed only for individually approved IDs in a SHA-256-bound report.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
