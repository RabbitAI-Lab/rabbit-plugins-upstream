## Description:

Versatile video generation with Kling v3 Omni that supports multimodal inputs, including prompts and images, to create dynamic videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Kling v3 Omni video generation service from an agent, supplying prompts and optional media and receiving generated media URLs or saved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media may be sent to dLazy's hosted API and media storage.

Mitigation: Review inputs before invoking the skill, avoid submitting sensitive media unless approved, and use the service only when hosted processing is intended.

Risk: Authentication can persist an API key under ~/.dlazy/config.json.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistence is not desired, rotate or revoke keys from the dLazy dashboard, and protect local user config files.

Risk: The skill depends on the pinned @dlazy/cli package and network endpoints api.dlazy.com and files.dlazy.com.

Mitigation: Review the pinned CLI package before installation and allow those endpoints only in environments approved for dLazy service use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results may be returned as hosted media URLs or downloaded locally with --save; asynchronous runs return a task identifier for polling.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
