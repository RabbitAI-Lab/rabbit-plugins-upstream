## Description:

Generates and edits detailed images from prompts and optional reference images through the dLazy image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images with fine details, text, and controlled composition using prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service.

Mitigation: Avoid private images and sensitive prompts unless dLazy processing is acceptable.

Risk: The third-party CLI can be installed globally and the API key saved locally.

Mitigation: Review the CLI before installation; use on-demand npx and DLAZY_API_KEY if persistent installation or stored credentials are unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI source (declared in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, Shell commands, Configuration guidance]

**Output Format:** [JSON response with image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports up to five reference images, aspect ratios through 21:9, and asynchronous generation. Bundled instructions pin the CLI to 1.2.3.]

## Skill Version(s):

1.2.14 (source: ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
