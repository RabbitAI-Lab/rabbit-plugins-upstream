## Description:

Use this skill for WeChat Official Account (mp.weixin.qq.com) requests involving reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage a WeChat Official Account through an OOMOL-connected account, including draft and material management, publishing, messaging, account utilities, and analytics retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, send, modify, and delete WeChat Official Account content through a connected OOMOL account.

Mitigation: Use it only with an account the agent is intended to manage, confirm exact payloads before write actions, and require explicit approval before destructive actions.

Risk: Installer snippets use remote shell execution for the oo CLI.

Mitigation: Install the oo CLI manually from a trusted source after reviewing the installer instead of letting an agent run curl|bash or irm|iex commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-weixin-official-account)
- [WeChat Official Account homepage](https://mp.weixin.qq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
