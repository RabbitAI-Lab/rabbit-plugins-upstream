## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos with support for multi-modal references, first/last frames, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Seedance 2.0 Fast hosted video-generation API from an agent, providing prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and dLazy cloud service.

Mitigation: Review the CLI package before use and run it with npx when avoiding a persistent global install is preferred.

Risk: Prompts and user-provided media may be sent to dLazy API and media storage endpoints for generation.

Mitigation: Avoid passing private media unless upload to the cloud service is intended.

Risk: The skill requires API-key authentication and may store credentials in local CLI configuration.

Mitigation: Use revocable API keys, rotate keys when needed, or provide DLAZY_API_KEY per invocation for tighter control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted result URLs; asynchronous calls may return a generateId for polling.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
