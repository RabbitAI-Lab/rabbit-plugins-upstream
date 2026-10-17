## Description:

Guides a single-resource PikPak link or magnet workflow from cloud task creation through local download verification, then prints a cleanup suggestion for manual review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized PikPak account holders use this skill to track one link or magnet from a cloud task to a local single-file download and review a cleanup command after checking the downloaded content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the wrong account or an unauthorized link can create cloud tasks or download unwanted content.

Mitigation: Confirm account ownership, source authorization, and destination before running; use only the intended PikPak account.

Risk: A local file hash does not prove the download matches the source, and a cleanup command could remove the wrong cloud object.

Mitigation: Check the downloaded content and current cloud object yourself; review the printed cleanup command before any manual deletion.

Risk: The state file contains task and file identifiers, and an untrusted CLI executable could act with the account's access.

Mitigation: Keep the state file private and do not set PIKPAK_BIN to an untrusted executable.

## Reference(s):

- [Upstream design and implementation boundaries](references/upstream-design.md)
- [rclone PikPak task handling (design reference, not release provenance)](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/helper.go#L186-L215)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands; local JSON state and download receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles one resource and one downloaded file per state file; prints rather than runs a cleanup command.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
