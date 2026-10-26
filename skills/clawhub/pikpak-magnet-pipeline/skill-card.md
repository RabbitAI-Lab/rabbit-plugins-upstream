## Description:

Guides users through explicitly authorized, single-resource PikPak task creation, status checks, local download, and a manually reviewed cleanup preview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and individual users use this skill to manage one authorized PikPak magnet or link through task tracking and a single-file local download. It keeps cleanup as a separately reviewed action rather than deleting cloud files automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow accesses a PikPak account and destination through a local CLI.

Mitigation: Use a trusted CLI in an environment you control, and explicitly authorize the account and destination before running it.

Risk: A failed download may leave a partial local file.

Mitigation: Inspect any partial file before retrying; do not assume a failed transfer left the destination unchanged.

Risk: A downloaded file may not match the intended source, and cloud deletion semantics are not guaranteed.

Mitigation: Verify the local content independently before separately authorizing any deletion; treat cleanup output as a preview, and note that real-account compatibility has not been established.

Risk: Local state files contain workflow receipts associated with an account and resource.

Mitigation: Keep state files private and out of shared locations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-magnet-pipeline)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak connected-app transfer quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions, shell commands, and JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One resource per state file and one downloaded file per task; cloud cleanup is not executed automatically.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
