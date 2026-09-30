## Description:

Syncs a profile by uploading a file selected from a service-provided manifest so the profile can be restored on another machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

People who want to restore their profile on another machine can use this skill to sync a file from their account's manifest to a trusted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A service-provided manifest can select a readable file anywhere under the user's home directory for upload without per-file confirmation, potentially exposing secrets or personal data.

Mitigation: Use only with a trusted service; inspect the exact file before upload, restrict the manifest to non-sensitive allowlisted paths, and require per-file consent.

Risk: Initialization writes a configuration file in the user's home directory.

Mitigation: Review and approve the configuration write before running initialization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/ledger-formatter-88335)

## Skill Output:

**Output Type(s):** [Guidance, JSON status]

**Output Format:** [Text guidance and JSON status object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sync can upload one readable file selected by the service's manifest.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
