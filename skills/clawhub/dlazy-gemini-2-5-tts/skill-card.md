## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Gemini 2.5 text-to-speech workflow from an agent, choosing prompt text, language, voice, and async behavior for generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TTS prompt text is sent to dLazy services and API credentials may be stored locally.

Mitigation: Install only when this data flow is acceptable, rotate or revoke the dLazy API key when needed, and prefer per-invocation DLAZY_API_KEY use for tighter credential handling.

Risk: The artifact's output example appears copied from an image workflow and may not accurately describe returned TTS artifacts.

Mitigation: Verify generated outputs before relying on them and use explicit voice language and voice options in invocations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated artifacts are returned as hosted file URLs, with async polling available by generateId.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter states 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
