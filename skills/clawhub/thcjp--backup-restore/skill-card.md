## Description:

Backup Restore helps agents plan scheduled backups and restores for MEMORY.md, training data, model weights, configuration files, skills, and Git repositories, including checksum verification, retention, and disaster drills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage backup, restore, rollback, migration, and disaster-drill workflows for critical agent and application data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restore workflows can overwrite live files or services.

Mitigation: Require explicit approval before restoring over live data, verify the selected backup ID and checksum, and document a rollback path before execution.

Risk: Retention cleanup can delete recovery points that may still be needed.

Mitigation: Confirm retention policy, protected backup sets, and minimum recovery coverage before enabling automated cleanup.

Risk: Backup jobs may include sensitive memory, training, model, configuration, or skill files.

Mitigation: Limit backup scope to approved paths and use only storage destinations that meet the environment's access-control and retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/backup-restore)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples and inline shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe backup identifiers, checksums, backup paths, verification status, and recovery errors.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
