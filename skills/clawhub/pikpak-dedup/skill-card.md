## Description:

Analyzes a specified PikPak folder for possible duplicate or alternate media releases and provides a report for manual review, without deleting files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can inspect a specifically authorized folder for possible duplicate or alternate media releases, compare suggested keepers, and review individual file IDs before any separate cleanup action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Name similarity or file metadata can suggest a false duplicate or an unsuitable file to keep.

Mitigation: Review each report and file ID manually; treat matches as candidates rather than proof of identical content.

Risk: Executing a printed removal command could delete a file without a confirmed recovery path.

Mitigation: Approve IDs against an unchanged report, do not run printed commands without separate authorization, and verify PikPak recovery behavior first.

Risk: A folder scan and local report can expose private file metadata.

Mitigation: Authorize only the specific folder needed and keep the report in a private, controlled location.

Risk: The optional referral code may benefit the publisher.

Mitigation: Ignore the referral code unless you intentionally choose to use it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-dedup)
- [Upstream design notes](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Human-readable or JSON analysis report; optionally printed cleanup commands after explicit approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Name-based matches are candidates, not verified identical files; commands are printed, not executed.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
