## Description:

Generates images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts or transform reference images with Doubao Seedream 4.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's cloud service.

Mitigation: Submit only content and files approved for sharing with dLazy.

Risk: The CLI stores an API key locally, and image-generation requests may incur charges.

Mitigation: Protect and rotate the API key if exposed; confirm paid requests before running them.

Risk: Generic image-generation requests may unintentionally invoke this external provider.

Mitigation: Use explicit Seedream or dLazy requests before invoking the skill.

## Reference(s):

- [dLazy CLI project (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON with hosted image URLs; optionally a downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an immediate image URL.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
