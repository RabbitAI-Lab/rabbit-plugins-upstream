## Description:

Selects a dLazy audio model for text-to-speech, music, dialogue, or sound-effect generation from a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run audio generation, text-to-speech, dialogue, music, and sound-effect workflows through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI uses a saved dLazy API key and sends prompts to dLazy.

Mitigation: Use a dedicated, revocable key and avoid sending sensitive prompts.

Risk: Local media paths passed to the CLI may be uploaded to dLazy.

Mitigation: Confirm files and permissions before supplying local paths.

Risk: The audio skill also includes non-audio image and video workflows.

Mitigation: Restrict use to audio commands unless an image or video operation is explicitly requested.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI JSON responses with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned by link; an authenticated dLazy account is required.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
