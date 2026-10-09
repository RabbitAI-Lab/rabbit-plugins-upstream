## Description:

Selects a dLazy model to generate images, video, or audio from a user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select a dLazy model and generate or edit images, videos, and audio from prompts and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files unless you are comfortable sharing them with dLazy.

Risk: Generation may consume paid credits, especially when broad trigger words select this skill.

Mitigation: Confirm the intended model and cost before running generation commands.

Risk: Logging in can store an API key on a shared device.

Mitigation: Use DLAZY_API_KEY for a single session or remove and revoke the stored key after use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Media links]

**Output Format:** [Markdown with shell commands and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requires a dLazy API key and may consume credits; media results are hosted by dLazy.]

## Skill Version(s):

1.3.27 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
