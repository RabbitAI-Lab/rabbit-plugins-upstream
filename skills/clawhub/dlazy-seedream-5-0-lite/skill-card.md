## Description:

Generate images from text prompts or reference images using Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image or reference-image-based generation and retrieve the resulting image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be uploaded to the dLazy cloud service, and generated images are hosted there.

Mitigation: Use the tool only for content you are comfortable sharing with dLazy.

Risk: Login may save an API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the pinned npm CLI and its linked source before installing when supply-chain assurance is needed.

Risk: The optional save command writes an image to a local path.

Mitigation: Use --save only with an intended destination path.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source (linked by skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task IDs and downloads to a chosen local path.]

## Skill Version(s):

1.3.23 (source: ClawHub release; bundled skill files list 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
