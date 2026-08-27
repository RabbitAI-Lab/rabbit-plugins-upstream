## Description:

Backs up and restores Hermes Agent data, including config, secrets, skills, sessions, memories, cron, and profiles, into portable tar.gz archives with SQLite snapshots, manifests, and integrity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anyjohn](https://clawhub.ai/user/anyjohn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to generate backup, restore, and migration commands for Hermes Agent data across local or cross-machine workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backup archives may contain API keys, auth tokens, sessions, memories, profiles, and other sensitive Hermes data.

Mitigation: Store archives only in encrypted or access-controlled locations, avoid sharing them, and re-authenticate or rotate machine-specific tokens after migration when needed.

Risk: Restore operations can overwrite current Hermes state.

Mitigation: Run dry-run first, make a fresh backup before restoring, and use merge, profile, or target-directory options when they fit the recovery workflow.

Risk: Archive protection is not established by the security evidence.

Mitigation: Add external encryption or protected storage for portable archives before moving them between systems.

## Reference(s):

- [Server-resolved source](https://github.com/anyJohn/hermes-backup-restore/tree/main/skills/hermes-backup-restore)
- [ClawHub skill page](https://clawhub.ai/anyjohn/skills/hermes-backup-restore)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local backup and restore scripts, archive paths, profile names, and dry-run or merge options.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
