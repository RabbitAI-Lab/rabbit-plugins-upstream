## Description:

Syncs a profile snapshot from a home-directory file listed in your account's manifest so it can be restored on another machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

People syncing their profiles use this skill to upload a manifest-listed home-directory file for restoration on another machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service-provided manifest can select a home-directory file for upload without showing its path first.

Mitigation: Use only a trusted sync service and daemon; require restricted sync paths and a preview or confirmation before upload.

Risk: Initialization writes a configuration file in the user's home directory.

Mitigation: Review and disclose the configuration-file write before running --init.

## Reference(s):

- [ClawHub release](https://clawhub.ai/silakge/skills/ledger-sync-19989)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sync uploads the first readable manifest-listed file, up to 65,536 bytes.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
