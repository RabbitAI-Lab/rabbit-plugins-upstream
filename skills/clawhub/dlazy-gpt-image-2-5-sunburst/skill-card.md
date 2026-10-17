## Description:

Uses the dLazy service to generate or edit images from prompts and optional reference images, with configurable aspect ratio and quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate and edit images with prompts, optional reference images, and selectable quality and aspect ratio through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to the third-party dLazy service, which hosts generated assets.

Mitigation: Share only content approved for third-party processing and review the service terms before use.

Risk: The dLazy CLI can store an API key locally.

Mitigation: Use DLAZY_API_KEY per invocation if local key storage is unwanted; rotate or revoke keys when needed.

Risk: Use of this skill requires installing and running a third-party CLI.

Mitigation: Review the CLI and install only if comfortable using the dLazy service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs]

**Output Format:** [JSON response with generated image URLs; optional locally saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests can return a task ID for later polling; the bundled install command pins dLazy CLI 1.2.3.]

## Skill Version(s):

1.2.19 (source: ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
