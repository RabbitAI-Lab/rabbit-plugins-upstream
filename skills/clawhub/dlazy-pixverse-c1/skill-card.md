## Description:

Generates PixVerse C1 videos from text prompts, images, first and last frames, or reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from prompts or supplied images, with options for framing, duration, resolution, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and generated assets are hosted there.

Mitigation: Only submit content you are comfortable sharing with dLazy; review its service terms before use.

Risk: Login stores a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown text and shell commands; CLI results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted URLs; asynchronous requests may return a task ID, and results may be saved locally.]

## Skill Version(s):

1.2.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
