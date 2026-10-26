## Description:

Generates high-fidelity vector illustrations from text prompts using Recraft V4 Pro Vector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use the skill to create high-quality vector assets and detailed illustrations from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for cloud processing, and generated assets are hosted by its service.

Mitigation: Use the skill only when that data transfer is acceptable; avoid submitting sensitive prompts or media.

Risk: The skill requires a dLazy API key and generation can consume service credits.

Mitigation: Keep the API key private, consider environment-variable authentication, and use --dry-run to review the request and estimated cost.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing generated image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are provided as hosted image URLs; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
