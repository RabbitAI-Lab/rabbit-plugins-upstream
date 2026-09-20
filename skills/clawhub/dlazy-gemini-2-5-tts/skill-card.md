## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and automation agents use this skill to generate Mandarin or English speech from text through the dLazy Gemini 2.5 TTS CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected parameters, and generated media are handled by dLazy's hosted service.

Mitigation: Use the skill only for content that can be sent to dLazy and review the service before processing sensitive data.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Prefer per-invocation environment variables or rotate and revoke organization keys when access changes.

Risk: Local file paths supplied to compatible media parameters may upload those files to dLazy storage.

Mitigation: Provide local file paths only when upload is intended and avoid sensitive local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted URLs; async runs may return a generation task ID.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
