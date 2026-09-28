## Description:

Generates images from text and edits or combines images using reference inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit and combine reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive prompts or files without authorization.

Risk: The third-party CLI may be installed globally, and login stores an API key locally.

Mitigation: Use the on-demand npx option to avoid a persistent global install; rotate or revoke the API key when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI repository (CLI metadata link; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs]

**Output Format:** [JSON result with image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, image size, format and quality options; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
