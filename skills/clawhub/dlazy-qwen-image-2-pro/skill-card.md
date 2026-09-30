## Description:

Guides agents to generate images from text prompts with Qwen Image 2 Pro through the dLazy CLI, including optional reference images and saved outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ClawHub users can direct an agent to create images from text prompts, optionally using reference images, and retrieve generated image links or save the results locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided local image files are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or files unless the external service is approved for them.

Risk: Authentication can save an API key in the local dLazy configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent key storage is unsuitable.

Risk: Using this skill installs or invokes the external @dlazy/cli package.

Mitigation: Review the package and linked CLI repository before installation when package provenance checks are required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions and JSON image-result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted image URLs or an asynchronous task ID; --save can download an image locally.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
