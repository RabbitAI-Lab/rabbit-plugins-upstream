## Description:

Quark Drive helps agents authenticate with Quark Cloud Drive, upload and read files, save shared links, search and organize drive content, create shares, and answer questions over drive files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Quark Cloud Drive through a CLI-backed workflow for authentication, file transfer, search, sharing, save-as operations, media organization, and file-based AI summarization or question answering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can update itself from a remote service, modify local skill files, and install dependencies with sudo on some systems.

Mitigation: Install or update only from a trusted Quark Drive publisher context, review the installer behavior before execution, and prefer constrained environments for evaluation.

Risk: The skill sends exact prompt text and a session id for tracking.

Mitigation: Avoid using the skill with secrets, confidential prompts, or sensitive documents unless that prompt tracking is acceptable.

Risk: Cloud-drive artifacts may be stored locally during file operations.

Mitigation: Review local runtime and artifact directories after sensitive operations and clear generated files according to local data-handling requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive)
- [Publisher Profile](https://clawhub.ai/user/quarkdrive)
- [Quark Drive](https://pan.quark.cn)
- [Authentication and Account Management](artifact/references/auth.md)
- [File Upload](artifact/references/file-upload.md)
- [File Search](artifact/references/file-search.md)
- [File Sharing](artifact/references/file-share.md)
- [AI Assistant](artifact/references/assistant.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and NDJSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and a Quark Drive account authorization before cloud-drive operations.]

## Skill Version(s):

1.0.15 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
