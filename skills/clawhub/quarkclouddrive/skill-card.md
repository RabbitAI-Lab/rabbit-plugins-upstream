## Description:

quarkclouddrive lets agents authenticate to Quark Drive and use its CLI to search, upload, download, share, transfer saved shares, organize media, batch rename files, and summarize or answer questions about cloud files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to operate a Quark Drive account from chat, including file search, upload, download, sharing, share transfer, media organization, batch renaming, and file Q&A. It is suited to users who want cloud-drive actions and assistant-backed file understanding without leaving the agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and mutate Quark Drive files through authenticated CLI commands.

Mitigation: Install only if the publisher is trusted, bind the intended account, and review actions before upload, move, share, transfer, rename, or read operations.

Risk: Raw user prompts and selected file contents may be sent to Quark services for tracking, summaries, and Q&A.

Mitigation: Avoid sensitive prompts or files unless that data flow is acceptable, and adjust the Quark Drive authorization scope where the service allows it.

Risk: The installer can download updates and may attempt privileged Node.js installation on Linux systems.

Mitigation: Prefer installing Node.js manually, review install or update prompts, and run the skill only in trusted agent environments.

Risk: Local authorization and task state can persist after use.

Mitigation: Use the documented unauthorize or uninstall flow when access should be revoked, and protect the local agent profile that stores configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive)
- [Quark Drive](https://pan.quark.cn)
- [Authorization and account management](references/auth.md)
- [AI assistant capabilities](references/assistant.md)
- [File search](references/file-search.md)
- [File operations](references/file-ops.md)
- [File upload](references/file-upload.md)
- [File read](references/file-read.md)
- [Share transfer](references/file-saveas.md)
- [File sharing](references/file-share.md)
- [Media organization](references/file-organize.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with shell command invocations; CLI results may include NDJSON or JSONL artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16 and Quark Drive authorization; cloud-drive operations can create, move, upload, share, transfer, rename, summarize, and read files depending on the selected command.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
