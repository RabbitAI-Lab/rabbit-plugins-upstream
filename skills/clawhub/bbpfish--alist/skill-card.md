## Description:

alist full-featured API client for file system operations, storage and driver management, user and metadata management, settings and task management, indexing, backup and restore, SSH/SFTP, audit logs, announcements, 2FA, SSO, scraping diagnostics, token management, and retries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bbpfish](https://clawhub.ai/user/bbpfish)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to let an agent administer an Alist server through CLI commands or a Python client, including file operations, storage, users, settings, tasks, backups, SSH/SFTP, 2FA, SSO, and scraping diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles powerful Alist administrator credentials and caches authentication tokens.

Mitigation: Install only from a trusted source, prefer HTTPS endpoints, avoid placing passwords or API keys directly in shell commands, and clear or protect the token cache.

Risk: The skill can perform destructive or sensitive operations such as delete, restore, clear, upload, download, SSH, SSO, and 2FA changes.

Mitigation: Use least-privilege Alist accounts and manually review those operations before allowing an agent to execute them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bbpfish/skills/alist)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)
- [Alist client script](artifact/scripts/alist_client.py)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke authenticated Alist administrator operations through generated commands or Python API usage.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
