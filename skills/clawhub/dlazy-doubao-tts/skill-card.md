## Description:

Helps agents synthesize spoken audio from text using Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users generate spoken narration from text, choosing a language, voice, and speaking speed and optionally saving the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and selected voice settings are sent to the third-party dLazy cloud service, which hosts generated files.

Mitigation: Avoid submitting sensitive text unless sharing it with dLazy is acceptable; review hosted output before sharing.

Risk: Authentication can save a dLazy API key in local configuration, and supplied file paths may trigger uploads.

Mitigation: Protect the local API key and provide private file paths only when upload is intended.

Risk: The documented language default is Chinese, and the example result depicts an image rather than audio.

Mitigation: Select the intended language and voice explicitly, and verify the actual generated file type.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is available through hosted result links and can optionally be saved locally.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
