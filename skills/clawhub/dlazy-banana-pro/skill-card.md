## Description:

Generate and edit images with Nano Banana Pro using text prompts and optional image references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to generate or edit images through the dLazy Nano Banana Pro CLI with text prompts, reference images, aspect ratio, size, and save options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy's hosted image service.

Mitigation: Avoid passing private files unless upload is intended, and use the service only when the user accepts the cloud-processing model.

Risk: The skill installs or runs a third-party CLI that uses a saved dLazy API key.

Mitigation: Prefer npx or an isolated environment when possible, review the linked source and package provenance, and rotate or revoke the API key if trust changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated image URLs or asynchronous task identifiers from the dLazy CLI.]

## Skill Version(s):

1.2.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
