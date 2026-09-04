## Description:

Quark Drive Skill for authorizing a Quark Drive account, uploading and reading files, sharing and saving shared links, searching cloud files, organizing media, and using Quark Drive AI assistant features for file summaries and Q&A.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Quark Drive accounts: authorize access, upload and read files, share files, save shared links, search cloud files, organize personal media, and run file-summary or Q&A workflows over cloud content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can fetch updated skill code from a Quark remote endpoint and may install Node.js prerequisites.

Mitigation: Install only after reviewing install.sh, prefer installing Node.js independently, and trust the publisher and remote update endpoint before execution.

Risk: Prompts and session identifiers are forwarded to the CLI for service-quality tracking.

Mitigation: Avoid including secrets or sensitive data in prompts passed to this skill.

Risk: Search, AI analysis, sharing, organizing, and file operations act on the authorized Quark Drive account and authorization scope.

Mitigation: Check the Quark authorization scope before use and confirm destructive or account-changing actions such as uninstall, authorization revocation, sharing, moving, or large media organization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive)
- [Quark Drive](https://pan.quark.cn)
- [Assistant capabilities](references/assistant.md)
- [Authorization and account management](references/auth.md)
- [File operations](references/file-ops.md)
- [Media organization](references/file-organize.md)
- [File reading](references/file-read.md)
- [Save shared links](references/file-saveas.md)
- [File search](references/file-search.md)
- [File sharing](references/file-share.md)
- [File upload](references/file-upload.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and NDJSON-aware result handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16 and Quark Drive authorization for account-scoped operations.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
