## Description:

Automatically selects a suitable dLazy CLI audio or text-to-speech model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to select a dLazy audio model and generate speech, dialogue, music, or sound effects from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and generated output URLs are hosted by its media service.

Mitigation: Review dLazy's privacy terms and upload only files intended for the service.

Risk: Audio generation can consume paid account credits.

Mitigation: Check the account's credit balance and expected usage before generating.

Risk: The external CLI runs locally and stores the API key in user configuration.

Mitigation: Review the pinned CLI dependency before installation and protect the saved API key.

## Reference(s):

- [dLazy CLI (external dependency)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Guidance]

**Output Format:** [Generated audio files or audio URLs; CLI responses use JSON envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected model determines available voice, language, duration, and style options.]

## Skill Version(s):

1.3.37 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
