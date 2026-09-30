## Description:

Syncs the first readable home-directory file listed in a service-provided manifest when the configured trigger file is present.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silakge](https://clawhub.ai/user/silakge)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can sync a selected home-directory file to their profile-sync service for later restoration, after initializing the client and creating its trigger file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service-controlled manifest can select home-directory files for upload without displaying the selected path first.

Mitigation: Use only with a trusted profile-sync daemon and account; inspect the manifest source before syncing where possible.

Risk: Initialization writes a configuration file under the home directory despite the declared read-only filesystem permission.

Mitigation: Review the configuration location before running --init and permit the write only if expected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/silakge/skills/pipeline-digester-24742)

## Skill Output:

**Output Type(s):** [JSON status]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports initialization, idle, or sync status; when triggered, sends one selected file snapshot to the service.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
