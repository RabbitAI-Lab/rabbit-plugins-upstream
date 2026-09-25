## Description:

Guides developers through backing up, restoring, and migrating local development environments, including configuration, repositories, credentials, software, and AI agent state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[futrixdev](https://clawhub.ai/user/futrixdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to plan and carry a local development environment between macOS or Linux machines, then restore selected files, repositories, software, credentials, and AI coding agent state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A custom HTTP download source can expose the installer to a substituted executable.

Mitigation: Use the default HTTPS release path; do not set ENVRELAY_DOWNLOAD_URL to an HTTP mirror, and review the install dry run first.

Risk: Backups may contain sensitive credentials and local development state.

Mitigation: Review each credential directory before carrying it, keep the backup encrypted, and enter the passphrase only in the user's terminal.

Risk: Restored agent hooks, MCP servers, and plugins can execute or steer behavior on the destination machine.

Mitigation: Review each extension and its commands with the user before restoring it.

## Reference(s):

- [EnvRelay on ClawHub](https://clawhub.ai/futrixdev/skills/envrelay)
- [EnvRelay homepage](https://envrelay.com/)
- [What to carry](artifact/references/what-to-carry.md)
- [Credential handling](artifact/references/credential-locations.md)
- [AI coding agent state](artifact/references/ai-agents.md)
- [Backup manifest](artifact/references/manifest.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance and commands; JSON manifest and local encrypted backup file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User confirms what is carried and enters the encryption passphrase directly in their terminal.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
