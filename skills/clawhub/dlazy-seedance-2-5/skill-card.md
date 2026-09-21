## Description:

视频生成 Seedance 2.5 helps agents run dLazy's hosted Seedance 2.5 video generation CLI for prompt-driven video creation with optional image, video, audio, and first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Seedance 2.5 video generation workflow from an agent, providing prompts and optional media references to produce hosted video output or save generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and hosted service.

Mitigation: Confirm the user is comfortable using the pinned @dlazy/cli package and dLazy service before installation or execution.

Risk: Prompts and referenced media files are sent to dLazy endpoints for generation.

Mitigation: Avoid submitting sensitive prompts or media unless the user has approved that disclosure.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied through DLAZY_API_KEY.

Mitigation: Use normal credential handling, prefer per-invocation environment variables where appropriate, and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by dLazy; async runs may return a generateId for later polling.]

## Skill Version(s):

1.2.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
