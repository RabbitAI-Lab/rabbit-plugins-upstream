## Description:

Generate natural-sounding multilingual speech from text using Gemini 2.5 TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and other users can turn text into Chinese or English speech with a choice of voices via the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied files may be sent to dLazy's hosted service, including content referenced from stdin or prior outputs.

Mitigation: Share only content intended for dLazy; avoid secrets, private documents, and broad stdin or prior-output references.

Risk: Using the CLI requires a dLazy API key that may be saved locally.

Mitigation: Keep the key private, restrict access to its storage, and rotate or revoke it if exposed.

Risk: The documented example shows an image result despite describing text-to-speech output.

Mitigation: Confirm the returned media type is audio before using or sharing the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Text with CLI commands and JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful results may include a hosted media URL; asynchronous calls may return a task ID instead.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
