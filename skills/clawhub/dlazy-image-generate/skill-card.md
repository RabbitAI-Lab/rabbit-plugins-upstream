## Description:

Selects a dLazy image model for a user's prompt and guides image generation or editing through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose a dLazy image model and generate, edit, upscale, or vectorize visuals from prompts and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media may be sent to dLazy services.

Mitigation: Do not provide sensitive prompts or files unless you intend to share them with dLazy.

Risk: Generation can consume paid API credits.

Mitigation: Confirm available credits and expected usage before running generation commands.

Risk: Logging in can store an API key locally.

Mitigation: Use a per-invocation API key or the on-demand CLI path if you want less persistent setup.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image or vector URLs may point to dLazy-hosted files.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
