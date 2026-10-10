## Description:

Generates and edits images from text prompts and optional reference images using the dLazy-hosted GPT Image 2.5 Sunburst service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit detailed images, including compositions with in-image text and reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or media unless approved for the service.

Risk: Installing and running the third-party CLI requires trusting its code.

Mitigation: Review the CLI before use; use the documented npx option if you prefer not to keep a global installation.

Risk: An API key is required for requests.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Image URLs, Image files]

**Output Format:** [JSON with generated image links; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image link.]

## Skill Version(s):

1.2.16 (source: ClawHub release; bundled skill frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
