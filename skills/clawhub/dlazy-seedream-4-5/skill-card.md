## Description:

Generates images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text or transform images using reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's cloud service.

Mitigation: Share only content you are authorized to upload; review inputs before sending.

Risk: Authentication requires a dLazy API key, which the CLI can save locally.

Mitigation: Use a per-invocation DLAZY_API_KEY when local credential storage is undesirable.

Risk: Image generation may consume paid credits.

Mitigation: Confirm intent for generic image-generation requests and use a cost-estimating dry run when appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON result with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID instead of an immediate image.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
