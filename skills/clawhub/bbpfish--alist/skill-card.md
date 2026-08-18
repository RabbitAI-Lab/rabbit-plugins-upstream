## Description: <br>
alist provides a full-featured REST API client for managing files, storage drivers, users, metadata, settings, tasks, indexes, backups, SSH/SFTP, audit logs, announcements, 2FA, SSO, and scraping diagnostics with token management and retries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbpfish](https://clawhub.ai/user/bbpfish) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to let an agent administer an alist instance through REST API calls and CLI/Python workflows, including file operations, storage management, user administration, task cleanup, backups, and diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant broad destructive administrative control over an alist instance. <br>
Mitigation: Install it only for intended alist administration and use a least-privileged API key or account where possible. <br>
Risk: Vague prompts could trigger destructive file, storage, user, or task actions. <br>
Mitigation: Require explicit review before running delete, move, storage, user, task cleanup, backup restore, or similar administrative commands. <br>
Risk: Login tokens may be stored locally with limited safeguards. <br>
Mitigation: Protect or delete the local token cache after use, especially on shared systems. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/bbpfish/skills/alist) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with command examples, Python snippets, configuration guidance, and JSON-like API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform authenticated alist API calls and local token caching when its bundled client is executed.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and ClawHub release evidence; changelog top entry is 1.0.0 released 2026-06-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
