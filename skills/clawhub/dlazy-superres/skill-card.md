## Description:

This skill enhances low-resolution images with dLazy's super-resolution CLI and returns an enhanced image URL, with optional local saving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and other external users use this skill to upscale low-resolution images through dLazy's hosted super-resolution service and receive an enhanced image URL. It is suited for restoring low-resolution visual assets and optionally saving the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and request parameters are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with images intended for upload to dLazy's service, and review the service terms before processing sensitive content.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Prefer the DLAZY_API_KEY environment variable when a key should not be stored on disk, and rotate or revoke organization keys when needed.

Risk: The --save option writes generated outputs to a local path.

Mitigation: Use --save only with paths intentionally selected for the generated image output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands]

**Output Format:** [JSON containing generated image output metadata and a hosted image URL; optional downloaded image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with --no-wait and local result download with --save.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
