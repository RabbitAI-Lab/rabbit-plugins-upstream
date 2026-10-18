## Description:

Analyzes potential duplicate or alternate-version media in an authorized PikPak folder and produces a report for manual review without deleting files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can identify possible duplicate or alternate-version media within an explicitly authorized folder, compare suggested keepers, and review candidates before approving any separate action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning exposes file metadata from the selected PikPak folder.

Mitigation: Authorize only the intended folder and use a trusted PikPak CLI binary.

Risk: Name-based matches can suggest the wrong files for removal, and recovery is not guaranteed.

Mitigation: Review the report and each printed rm command; do not run commands without independently confirming targets and recovery behavior.

Risk: The optional referral code may attribute a signup to the sharer.

Mitigation: Decline or explicitly clear the referral code if affiliate attribution is unwanted.

## Reference(s):

- [PikPak Dedup release on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-dedup)
- [Upstream design and limitations](references/upstream-design.md)
- [Czkawka duplicate-checking methods (technical reference)](https://github.com/qarmin/czkawka/blob/eb8b91dbb4d25dff416202674ee0de84ee4b5e5c/instructions/Instruction_Core.md#L37-L47)
- [rclone hash comparison (technical reference)](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/fs/operations/operations.go#L48-L122)

## Skill Output:

**Output Type(s):** [JSON reports, Text summaries, Shell commands]

**Output Format:** [JSON or plain text; optionally printed PikPak CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidates are name-based, not confirmed content duplicates; approved commands are printed but never executed.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
