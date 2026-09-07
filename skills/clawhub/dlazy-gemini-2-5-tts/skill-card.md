## Description:

Generate multilingual, highly natural speech audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill through the dLazy CLI to generate Mandarin or English speech audio from text prompts with selectable Gemini 2.5 TTS voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and any selected local media files to dLazy cloud endpoints for processing and hosted output delivery.

Mitigation: Only pass files intended for upload, review the linked dLazy CLI project before installation, and prefer the pinned npx invocation if a persistent global binary is not desired.

Risk: The skill requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Treat the key as a credential and rotate or revoke it from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Audio URLs]

**Output Format:** [Markdown with inline bash commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated result URLs are hosted by files.dlazy.com.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter says 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
