## Description:

Generates images with the Kling Image O1 model from text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate or edit images with Kling Image O1 from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference files are sent to dLazy, and generated image URLs are hosted there.

Mitigation: Submit only prompts and files you are comfortable sharing with the service.

Risk: The skill depends on an external CLI and an organization API key.

Mitigation: Review the CLI before installation and protect or rotate the API key through the dLazy dashboard.

## Reference(s):

- [dLazy CLI project page (skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image files with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and can optionally be saved to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
