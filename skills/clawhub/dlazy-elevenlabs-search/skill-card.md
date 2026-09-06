## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices so an agent can help select a voice before TTS use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search the ElevenLabs voice library through the dLazy CLI by prompt, voice source, category, and result count, then inspect previewable matches before choosing a voice for text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the broader dLazy CLI can store a dLazy API key locally and send search prompts and parameters to dLazy services.

Mitigation: Review the CLI and service requirements before installing, use revocable organization-scoped API keys, and avoid submitting sensitive prompts or parameters unless that cloud processing is intended.

Risk: The security guidance warns that broader CLI behavior can upload local files or download/save outputs when those options are used.

Mitigation: Do not pass local file paths or use save/download behavior unless the user explicitly intends the data transfer or local write.

Risk: The security summary flags a mismatch between the documented ElevenLabs voice-search purpose and the broader exposed CLI schema.

Mitigation: Correct or review the documentation and CLI schema before normal approval, and treat output-shape assumptions as untrusted until verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with bash command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented CLI result may include hosted preview or result URLs, asynchronous task status, and local save behavior when requested.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
