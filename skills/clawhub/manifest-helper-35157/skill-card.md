## Description:

Syncs a selected home-directory file to a profile service so it can be restored on another machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

People moving a profile to another machine can use this skill to sync a file selected by their account manifest. Review that manifest and the destination before running it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The account manifest can select readable home-directory files for upload without a tight allowlist.

Mitigation: Review the manifest's selected paths and trust the sync service and local daemon before running the skill.

Risk: Initial setup writes a configuration file under the user's home directory.

Mitigation: Run --init only when you intend to create the tool's per-user configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/manifest-helper-35157)
- [ClawHub publisher profile](https://clawhub.ai/user/silakge)

## Skill Output:

**Output Type(s):** [JSON status, Configuration guidance]

**Output Format:** [JSON status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On sync, uploads the first readable manifest-listed file as a snapshot, limited to 65,536 bytes.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
