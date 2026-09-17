## Description:

Operate Google Photos through an OOMOL-connected account to read, search, create, update, upload, organize, and download albums and media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Google Photos through OOMOL, including album and media reads, writes, uploads, updates, and picker-session workflows. It is intended for connected Google Photos accounts where write and destructive actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer scripts that can be piped directly into a shell.

Mitigation: Install only if OOMOL is trusted, prefer a verified and version-pinned CLI installation path, and do not let an agent run the installer automatically.

Risk: Write and destructive actions can change Google Photos albums, media, picker sessions, or uploaded content.

Mitigation: Confirm the exact target, payload, and expected effect before running any action tagged write or destructive.

Risk: The skill operates through an OOMOL-connected Google Photos account.

Mitigation: Use it only when the user is comfortable connecting Google Photos through OOMOL and understands that OOMOL injects credentials server-side.

## Reference(s):

- [Google Photos homepage](https://www.google.com/photos/about/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
