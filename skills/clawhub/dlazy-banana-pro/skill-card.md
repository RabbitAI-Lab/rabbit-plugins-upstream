## Description:

Helps agents generate and edit images from text prompts and reference images using Nano Banana Pro through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users create or edit images from prompts and optional reference images using dLazy's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files may be sent to dLazy's cloud service.

Mitigation: Avoid sensitive prompts or images unless the service's data handling is acceptable for the use case.

Risk: Authentication can store an API key on the user's device.

Mitigation: Protect local credentials and rotate or revoke keys if exposed.

Risk: Using the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the package and declared source before use in sensitive environments; use the pinned on-demand command to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source (declared in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and may be saved locally.]

## Skill Version(s):

1.2.35 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
