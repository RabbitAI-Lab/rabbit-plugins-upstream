## Description:

Generates images with Doubao Seedream 5.0 Lite from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts or transform reference images through dLazy's hosted Seedream service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI may store the API key in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if local key storage is unwanted.

Risk: Prompts, parameters, and selected local images are sent to dLazy's hosted service.

Mitigation: Avoid private prompts or files unless their upload is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and CLI JSON responses containing generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be downloaded to a local path; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
