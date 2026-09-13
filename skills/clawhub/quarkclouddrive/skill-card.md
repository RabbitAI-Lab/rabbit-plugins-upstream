## Description:

Quarkclouddrive helps an agent operate Quark Drive for authorization, file upload and download, sharing and save-as workflows, search, bulk rename and rollback, photo organization, and file summary or question-answering tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Quark Drive files, shares, authorization, search results, batch renames, photo organization, and file understanding workflows from natural-language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can replace the reviewed package with code and instructions retrieved from a remote update service.

Mitigation: Install only when the publisher and update service are trusted; review the installer and treat every update as a new security-sensitive package.

Risk: The skill requires sending the user's full original prompt to the CLI for session tracking.

Mitigation: Avoid secrets and sensitive personal data in prompts when invoking the skill.

Risk: The skill can perform broad Quark Drive operations, including sharing, moving, uploading, downloading, batch renaming, rollback, and photo organization.

Mitigation: Use the narrowest Quark Drive authorization available and require explicit user confirmation for sharing, destructive, or bulk file operations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/quarkdrive/skills/quarkclouddrive)
- [Publisher profile](https://clawhub.ai/user/quarkdrive)
- [Quark Drive](https://pan.quark.cn)
- [Authorization and account management](artifact/references/auth.md)
- [File search](artifact/references/file-search.md)
- [File upload](artifact/references/file-upload.md)
- [File operations](artifact/references/file-ops.md)
- [Read files](artifact/references/file-read.md)
- [Save shared files](artifact/references/file-saveas.md)
- [File sharing](artifact/references/file-share.md)
- [Photo organization](artifact/references/file-organize.md)
- [Assistant capabilities](artifact/references/assistant.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, file-operation summaries, and CLI result handling instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide an agent through Quark Drive commands that may upload, download, share, save, search, rename, organize, summarize, or ask questions over user files.]

## Skill Version(s):

1.0.20 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
