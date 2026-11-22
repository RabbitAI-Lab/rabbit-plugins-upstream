## Description:

Image generation skill. Automatically selects the best dlazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate, edit, upscale, or vectorize images through the dLazy CLI, selecting a suitable image model for each prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy hosted services, and the security review notes video and speech capabilities beyond the image-generation description.

Mitigation: Review the requested command and its inputs before use, avoid sending sensitive prompts or files, and confirm that any video or speech generation is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy service](https://dlazy.com)
- [dLazy CLI repository (listed in artifact metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, SVG graphics, URLs, JSON]

**Output Format:** [Generated asset URLs in a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can be passed between CLI commands using pipe references.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
