## Description:

Generates images from text and edits or combines images using reference inputs through GPT Image 2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts or edit images using reference inputs through dLazy's hosted image service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable sharing with dLazy; review selected files before use.

Risk: Logging in may store a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI repository (publisher metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs]

**Output Format:** [JSON response containing generated image URLs; optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, up to five reference images, and image size, format, and quality options.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
