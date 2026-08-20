## Description:

Generate multilingual, natural-sounding audio from text using Gemini 2.5 text-to-speech through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate Chinese or English text-to-speech audio through dLazy's hosted Gemini 2.5 TTS workflow. It provides authentication guidance, command examples, voice and language options, and async task handling for CLI-based audio generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TTS prompts, parameters, and explicitly referenced media files are processed by the dLazy hosted API.

Mitigation: Use the skill only for content that may be sent to dLazy, and avoid submitting sensitive data unless that use is approved.

Risk: The dLazy API key may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Keep the key scoped to the intended organization, rely on OS user file permissions, and rotate or revoke the key when access is no longer needed.

Risk: A global CLI installation persists a local command on the user's system.

Mitigation: Use the pinned npx invocation or review the pinned CLI source before choosing a global install.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio results and asynchronous task status are returned by the dLazy service, with hosted result URLs on files.dlazy.com.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
