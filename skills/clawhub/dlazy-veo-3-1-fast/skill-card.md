## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run the dLazy Veo 3.1 Fast CLI for short text-to-video, image-to-video, and video extension jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm CLI, which creates normal npm supply-chain risk.

Mitigation: Use the pinned on-demand npx path or an isolated install, and review the CLI package or source before use.

Risk: The CLI stores or uses a dLazy API key.

Mitigation: Protect the local config file or provide DLAZY_API_KEY per invocation, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and selected media files are uploaded to dLazy services.

Mitigation: Avoid sending sensitive prompts or media unless the dLazy service terms and data handling are acceptable for the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated media URLs or save generated assets through the dLazy CLI.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
