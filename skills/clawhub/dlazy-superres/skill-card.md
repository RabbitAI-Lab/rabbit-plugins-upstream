## Description:

Enhances low-resolution images and returns a URL for the upscaled result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to restore clarity and detail in low-resolution images using dLazy's hosted upscaling service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images are uploaded to dLazy's hosted service.

Mitigation: Only submit images approved for third-party processing.

Risk: Authentication uses an API key, which the CLI can store locally.

Mitigation: Use the key per invocation with DLAZY_API_KEY if persistent storage is unsuitable; rotate or revoke exposed keys.

Risk: Installing the CLI introduces third-party package code into the environment.

Mitigation: Use the documented pinned @dlazy/cli@1.2.3 version and review the package before running it.

Risk: The bundled --prompt example conflicts with the documented image option.

Mitigation: Use the documented --image option for actual upscaling requests.

## Reference(s):

- [dLazy CLI project (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image result URLs]

**Output Format:** [Markdown with inline commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service can return an asynchronous task ID instead of an immediate result URL.]

## Skill Version(s):

1.3.28 (source: ClawHub release; bundled frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
