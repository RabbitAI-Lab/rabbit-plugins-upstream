## Description:

Manage PikPak cloud storage via pikpakcli: browse, upload, download, delete, rename, share, offline download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cn-codegod](https://clawhub.ai/user/cn-codegod)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through PikPak cloud-drive management with pikpakcli, including browsing storage, checking quota, creating folders, uploading or downloading content, sharing, renaming, and deleting files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires PikPak account credentials for pikpakcli configuration.

Mitigation: Use it only when you trust the pikpakcli project and the execution environment where credentials will be configured.

Risk: The skill includes commands that delete cloud-drive files or folders.

Mitigation: Before deletion, require the agent to list the exact target paths and obtain explicit confirmation.

Risk: The documented workflow depends on an external pikpakcli tool built from source.

Mitigation: Review and trust the pikpakcli source before installation or use.

## Reference(s):

- [Server-resolved source repository](https://github.com/CN-CODEGOD/PIKSKILL)
- [pikpakcli project](https://github.com/52funny/pikpakcli)
- [Go installation documentation](https://go.dev/doc/install)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide actions that use PikPak account credentials and modify cloud-drive contents.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
