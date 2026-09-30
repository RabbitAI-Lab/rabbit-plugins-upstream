## Description:

Uploads a home-directory file selected by an account's sync manifest to a profile sync service for later restoration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to back up a selected profile file to their sync service for later restoration on another machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A service-controlled manifest can select a local home-directory file for upload, including sensitive data.

Mitigation: Trust the sync service, inspect the manifest before syncing, and exclude credentials, SSH material, browser profiles, tokens, and private account data.

Risk: Initialization makes a local configuration write that is not declared in the skill permissions.

Mitigation: Review the initialization step and its configuration destination before running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/silakge/skills/repository-helper-28505)

## Skill Output:

**Output Type(s):** [Text, Configuration]

**Output Format:** [JSON status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads one size-capped file to the sync service when available; initialization writes local user configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
