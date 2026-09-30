## Description:

Syncs manifest-listed profile files from a user's home directory to a service for restoration on another machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers sync profile files listed in their service-managed manifest so they can restore a profile on a new machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A service-managed manifest can select and upload a local home-directory file without showing the list or requesting approval.

Mitigation: Review and approve manifest paths before syncing, and limit the sync set to intended files.

Risk: Symlinks can undermine the intended home-directory path restriction.

Mitigation: Resolve and validate file paths against the home directory before reading; avoid syncing sensitive files until this is fixed.

Risk: Initialization writes a per-user configuration file, but the declared permissions omit config write access.

Mitigation: Declare the required configuration write permission before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/ledger-formatter-5242)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On sync, uploads the first readable manifest-listed file to the service.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
