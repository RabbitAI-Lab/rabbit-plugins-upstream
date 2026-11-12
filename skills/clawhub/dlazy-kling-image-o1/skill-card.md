## Description:

Generate images with Kling o1 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create images from text prompts or edit images using reference images with the Kling o1 model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files are sent to dLazy-hosted services, and generated output is hosted there.

Mitigation: Avoid sending sensitive material unless dLazy's data handling and service terms are acceptable for the use case.

Risk: The security review was partial: some local references could not be resolved, the installed CLI package was not scanned, and the scanner could not connect a login operation to the advertised image-generation purpose.

Mitigation: Review the unresolved references and CLI package before installation, and confirm the login flow is expected.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)

## Skill Output:

**Output Type(s):** [Image files, JSON metadata]

**Output Format:** [Generated image assets (PNG) with JSON result or task metadata and hosted URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be saved locally; asynchronous runs can return a task ID.]

## Skill Version(s):

1.3.38 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
