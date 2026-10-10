## Description:

Selects dLazy models to generate images, videos, and audio from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select dLazy generation models and create images, videos, or audio through its CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media files are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive content unless you are comfortable sharing it with dLazy.

Risk: Generation may use account credits, including when a vague request triggers generation.

Mitigation: Confirm the intended media and model before running an ambiguous generation request.

Risk: A global CLI installation and locally stored API key may persist on the user's device.

Mitigation: Use the pinned npx invocation or a per-invocation DLAZY_API_KEY when persistence is not wanted.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Media URLs]

**Output Format:** [Text guidance and CLI commands; CLI results are JSON with hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can chain generation commands using JSON output references.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
