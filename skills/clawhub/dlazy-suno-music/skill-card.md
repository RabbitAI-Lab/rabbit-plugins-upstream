## Description:

Helps agents generate music with or without vocals using inspiration or custom-lyrics mode through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request music with vocals or instrumental tracks, choosing automatic lyrics or supplying their own lyrics and style preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media may be sent to the dLazy hosted service, where generated assets are hosted.

Mitigation: Send only content you are comfortable sharing with dLazy and review its service terms before use.

Risk: The npm CLI requires an API key and login or manual setup can store it locally.

Mitigation: Review the CLI package before installing, protect the local key, and rotate or revoke it if exposed.

Risk: The documented output example describes an image rather than music and may mislead downstream handling.

Mitigation: Check returned media type and URL before using or distributing the generated asset.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI JSON results with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID; the documented example shows image data despite the music use case, so confirm actual media format.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
