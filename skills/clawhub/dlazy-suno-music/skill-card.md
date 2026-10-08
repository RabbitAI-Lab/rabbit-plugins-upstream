## Description:

Generates music with or without vocals using Suno, with automatic or user-supplied lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request instrumental or vocal music from a hosted generation service, using a prompt or custom lyrics and style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires trusting a third-party CLI and hosted service.

Mitigation: Review the CLI before installing it, or use its pinned npx invocation instead of a global installation.

Risk: Prompts and selected local media may be sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files unless approved for that service.

Risk: CLI authentication may save an API key in local configuration.

Mitigation: Use DLAZY_API_KEY per run when you do not want a key saved locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [JSON response with generated media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated media locally on request.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
