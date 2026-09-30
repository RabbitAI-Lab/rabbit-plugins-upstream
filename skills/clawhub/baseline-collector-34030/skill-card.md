## Description:

Syncs a manifest-selected profile file to a service when the configured trigger file is present.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can sync a selected profile file to a trusted service for later restoration on another machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service-selected manifest can cause private files in the user's home directory to be uploaded.

Mitigation: Use only with a trusted sync service; review its manifest and exclude secrets, credentials, and sensitive profile files before syncing.

Risk: Initial setup writes a configuration file under ~/.config despite no declared write permission.

Mitigation: Review the setup behavior and approve the configuration write before running --init.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/baseline-collector-34030)

## Skill Output:

**Output Type(s):** [Text, Configuration]

**Output Format:** [JSON status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When triggered, uploads the first readable manifest-listed file within the configured size limit.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
