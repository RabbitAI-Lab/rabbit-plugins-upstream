## Description:

Clone a reference voice and generate spoken audio from new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate spoken audio from text using a reference voice through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without permission may enable impersonation.

Mitigation: Confirm consent to clone the reference voice before use.

Risk: Prompts and reference audio are sent to dLazy's hosted service.

Mitigation: Only provide material you are comfortable sharing with dLazy.

Risk: Authentication may save an API key locally, and global npm installation persists the CLI.

Mitigation: Use DLAZY_API_KEY or the pinned npx command when local persistence is undesirable.

Risk: The documented example shows an image despite this being an audio-generation skill.

Mitigation: Treat the image-shaped example as a documentation error and inspect actual results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is returned via hosted result URLs; asynchronous requests may return a task ID instead.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
