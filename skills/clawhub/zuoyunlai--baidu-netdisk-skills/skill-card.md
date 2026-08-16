## Description:

Baidu Netdisk Skills helps agents manage Baidu Netdisk files under /apps/bdpan/ and back up or restore supported Claw agent memory through the bdpan CLI, with confirmation controls for high-impact operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to upload, download, transfer, share, search, move, copy, rename, create, and delete Baidu Netdisk files, and to back up or restore supported Claw agent memory. It is intended for explicit user-initiated file operations where credential handling, path limits, overwrite checks, and user confirmations matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's Baidu Netdisk account and install or run the bdpan CLI.

Mitigation: Install only after reviewing the skill and only if granting that account access is acceptable.

Risk: File operations and memory restore actions can overwrite, delete, share, or otherwise change cloud and local data.

Mitigation: Review exact local paths, Netdisk paths, share expiration, recipients, and restore overwrite lists before approving any operation.

Risk: Authorization codes or stored tokens could be exposed in shared, public, or logged terminals.

Mitigation: Avoid entering authorization codes in shared environments, do not expose token configuration files, and log out or uninstall when access is no longer needed.

Risk: Skill updates can modify local skill files.

Mitigation: Run updates only after an explicit user request and review update behavior before continuing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/baidu-netdisk-skills)
- [Skill Instructions](artifact/SKILL.md)
- [Authentication Guide](artifact/reference/authentication.md)
- [bdpan CLI Command Reference](artifact/reference/bdpan-commands.md)
- [Usage Examples](artifact/reference/examples.md)
- [Troubleshooting Guide](artifact/reference/troubleshooting.md)
- [Baidu Netdisk](https://pan.baidu.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown/text responses with inline shell commands and occasional JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local path checks, Netdisk path summaries, confirmation prompts, share links, and download progress updates.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
