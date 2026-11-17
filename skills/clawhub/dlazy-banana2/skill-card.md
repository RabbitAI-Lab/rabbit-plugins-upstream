## Description:

Generate and edit high-quality images with Nano Banana 2.0 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to create images from text prompts or edit supplied reference images through dLazy's Nano Banana 2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags the CLI login command as not clearly tied to the stated image-generation purpose, and notes that some reference checks were incomplete.

Mitigation: Review the CLI and its service before logging in; use the dLazy account and API key only if that service fits your needs.

Risk: The skill sends prompts to dLazy and uploads supplied local images to its media service for processing.

Mitigation: Submit only prompts and images that are appropriate to share with the service, and avoid including sensitive content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files (typically PNG) and a JSON result envelope with output URLs or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate from text or edit reference images; images may be saved locally or returned as hosted URLs.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
