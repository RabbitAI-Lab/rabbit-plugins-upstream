## Description:

Searches the ElevenLabs voice library by keyword, source, and category to help users choose voices using playable previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search for suitable ElevenLabs voices and listen to previews before using a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI and hosted service receive search prompts and parameters.

Mitigation: Review the CLI before installation and avoid sending sensitive prompts or parameters.

Risk: Using local media paths can upload files, while --save can download results to disk.

Mitigation: Pass media paths or use --save only when the transfer is intended.

Risk: The documentation includes generic generation and image-output examples that may not reflect voice-search results.

Mitigation: Check actual results and preview links before relying on or sharing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with voice-search summaries and optional preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice results and preview availability depend on the external service.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
