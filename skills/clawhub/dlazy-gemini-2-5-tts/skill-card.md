## Description:

Generates natural-sounding speech from text using Gemini 2.5 TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to request generated speech from text prompts, choosing a voice and Chinese or English voice language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files supplied to the CLI are sent to the dLazy service.

Mitigation: Only send content approved for a third-party service, and review the dLazy CLI and service before use.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Protect the key and local config, or pass the key for individual invocations when persistence is unwanted.

Risk: The voice language defaults to Chinese, which may not match the requested language.

Mitigation: Set the voice language explicitly when requesting English speech.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with CLI commands and generated-audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with output links or an asynchronous task identifier.]

## Skill Version(s):

1.3.30 (source: ClawHub release; artifact frontmatter states 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
