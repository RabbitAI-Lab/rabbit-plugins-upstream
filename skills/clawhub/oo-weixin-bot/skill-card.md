## Description:

Operates Weixin Bot through an OOMOL-connected account using the oo CLI to read inbound messages and send approved replies, media, and typing indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Weixin Bot account from an agent, including polling messages, downloading inbound media, and sending user-approved text, media, or typing updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include commands that execute remote installer scripts as local code.

Mitigation: Do not run the documented curl-to-shell or PowerShell installer unless the source is independently trusted; prefer a pinned, signed, or checksum-verified installer when available.

Risk: Write actions can send messages, media, or typing indicators through the connected Weixin Bot account.

Mitigation: Confirm the exact payload and effect with the user before executing any action tagged as write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-weixin-bot)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Weixin Bot Homepage](https://github.com/Tencent/openclaw-weixin)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before execution; connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
