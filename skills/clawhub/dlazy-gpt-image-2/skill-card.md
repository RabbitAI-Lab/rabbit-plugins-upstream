## Description:

Generates and edits images from text prompts and optional reference images using the dLazy-hosted GPT Image 2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images with reference inputs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be uploaded to the third-party dLazy service.

Mitigation: Review prompts and image inputs before submission; avoid sharing sensitive material.

Risk: Signing in can save an API key in local CLI configuration.

Mitigation: Review the dLazy CLI source before installation and protect or rotate the saved key as needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Image URLs in structured JSON, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-based generation and editing with up to five reference images; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
