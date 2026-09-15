## Description:

Feishu Custom Bot helps agents send Feishu/Lark custom bot messages through the OOMOL feishu_custom_bot connector using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Feishu Custom Bot action schemas and send text, image, rich-text post, interactive card, or shared-chat messages through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run remote installer scripts directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified package, pinned release, checksum, signature, or manual inspection before running installer commands.

Risk: The skill sends Feishu/Lark custom bot messages through a connected account.

Mitigation: Inspect the live action schema and confirm the exact message payload and effect with the user before allowing any post.

Risk: The security summary notes that the skill description is broader than the documented message-sending actions.

Mitigation: Use the skill only for documented Feishu/Lark custom bot message-sending actions unless updated evidence documents additional supported actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-feishu-custom-bot)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Feishu Custom Bot Homepage](https://www.feishu.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before write actions that send messages.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
