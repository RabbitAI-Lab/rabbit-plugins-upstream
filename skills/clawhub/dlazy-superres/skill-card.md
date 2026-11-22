## Description:

Provides a command workflow intended to upscale images, improve clarity and detail, and return an enhanced image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can use the dLazy super-resolution workflow to improve low-resolution image assets and obtain a URL for the resulting image. Confirm the current CLI behavior before relying on the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation says requests go to dLazy services and local image files are uploaded for processing.

Mitigation: Send only images you are authorized to share, and review the service terms before using sensitive images.

Risk: The skill requires a dLazy API key, while the security guidance says external CLI and authentication details were not verified by the partial scan.

Mitigation: Review the pinned CLI package before installation, use a dedicated API key, and rotate or revoke it when needed.

Risk: The security guidance says the inspected instructions do not demonstrate the advertised image-upscaling workflow.

Mitigation: Check the current CLI help and verify the result with a non-sensitive sample before relying on the workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URL, JSON, Shell commands, Guidance]

**Output Format:** [JSON result with an enhanced image URL, plus command-line text or an asynchronous task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result image URL is hosted by dLazy; asynchronous runs may initially return a task identifier.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
