## Description:

音乐生成 Suno Music generates Suno-style music from prompts, supporting inspiration mode with automatic lyrics and custom mode with manual lyrics for vocal or instrumental output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Suno music generation workflow from an agent, creating vocal or instrumental music from prompt, style, title, and lyric settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly passed to the skill may be uploaded to dLazy services for generation.

Mitigation: Avoid sending sensitive prompts or files unless the user's organization has approved dLazy for that data.

Risk: Login may save a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials or npx when persistence is undesirable, keep the config file restricted to the OS user, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs or asynchronous task status, plus concise user-facing guidance for authentication, balance, or API failures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are hosted as dLazy file URLs; prompts and explicit media inputs are sent to dLazy's hosted API.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
