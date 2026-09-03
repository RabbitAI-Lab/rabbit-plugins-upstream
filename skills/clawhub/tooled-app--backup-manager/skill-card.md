## Description:

Create and maintain a per-project backup routine: define what to back up with include and exclude rules, where to store it, and how often; then take, verify, and rotate backups automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and project maintainers use this skill to establish and run practical backup routines before major changes, destructive operations, scheduled maintenance, or restore checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A backup can omit important project data or include rebuildable files if the backup scope is unclear.

Mitigation: Define source-of-truth folders, include rules, and exclude rules before creating the archive, then verify expected critical files are present.

Risk: Secrets or private data can be copied into shared or cloud-synced backup locations.

Mitigation: Decide the secrets policy before installation; exclude files such as .env by default or place sensitive material in a separately encrypted archive.

Risk: Automatic rotation can remove useful backup history if retention is too aggressive or the newest backup is invalid.

Mitigation: Confirm retention count and destination policy in advance, verify the newest archive before deletion, and report any removed backups.

## Reference(s):

- [Backup Manager on ClawHub](https://clawhub.ai/tooled-app/skills/backup-manager)
- [Tooled](https://tooled.pro)
- [OpenClaw](https://openclaw.ai)
- [IKKF](https://ikkf.info)
- [Demystify](https://demystified.website)
- [Ollama](https://ollama.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands, file paths, backup logs, and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce backup archives, checksums, retention actions, and restore or verification summaries when executed by an agent.]

## Skill Version(s):

1.32.427 (source: server release metadata; skill frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
