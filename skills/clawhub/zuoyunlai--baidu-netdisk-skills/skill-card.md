## Description:

Baidu Netdisk Skills helps an agent manage Baidu Netdisk files with bdpan commands and perform supported agent memory backup, listing, and restore workflows after explicit user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to upload, download, transfer, share, search, move, copy, rename, create, or delete files in Baidu Netdisk. It also supports explicit backup, listing, and restore of supported Claw agent memory files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the release as suspicious because install, update, uninstall, and memory restore paths have enough local-file and agent-memory authority to require review before use.

Mitigation: Install only when the publisher is trusted, avoid --yes for install, update, uninstall, and memory restore, and review update sources and checksums before approving changes.

Risk: Memory restore can overwrite local agent memory files.

Mitigation: Back up agent workspace memory before restore and review the restore target and affected files before confirming execution.

Risk: Baidu Netdisk operations can overwrite, delete, or publicly share cloud or local files when used incorrectly.

Mitigation: Review the proposed operation scope, confirm risky write or share actions explicitly, and verify BDPAN_CONFIG_DIR and BDPAN_INSTALL_DIR are not set to unsafe paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/baidu-netdisk-skills)
- [Authentication guide](reference/authentication.md)
- [bdpan CLI command reference](reference/bdpan-commands.md)
- [Usage examples](reference/examples.md)
- [Troubleshooting guide](reference/troubleshooting.md)
- [Development notes and safety reminders](reference/notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON command output when bdpan commands are requested with JSON formatting.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
