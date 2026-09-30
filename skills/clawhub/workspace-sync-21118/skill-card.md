## Description:

Syncs files listed in an account manifest to a profile service so they can be restored on a new machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

People syncing a workspace profile can upload manifest-selected files to their account's sync service for restoration on another machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A service-selected symlink may cause a file outside the intended home-directory scope to be uploaded.

Mitigation: Review before installing; use only with a trusted sync service and manifest, and prefer a version that resolves paths and rejects symlink escapes before uploading.

## Reference(s):

- [Workspace Sync 21118 on ClawHub](https://clawhub.ai/silakge/skills/workspace-sync-21118)

## Skill Output:

**Output Type(s):** [Guidance, JSON status]

**Output Format:** [Markdown guidance and JSON status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Syncs the first readable manifest-selected file, up to 65,536 bytes, to the service.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
