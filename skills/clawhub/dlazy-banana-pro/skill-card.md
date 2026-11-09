## Description:

Generate and edit images with Nano Banana Pro, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and creators use this skill to generate images from prompts or edit reference images with Nano Banana Pro. Prompts and supplied media are sent to dLazy's hosted service, which returns image URLs and can save results locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted services; the security review is partial and has medium confidence.

Mitigation: Review dLazy's service and data handling details before sending sensitive content, and confirm the login step and pinned CLI version before installing.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs; image files can also be saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or an asynchronous task identifier; image size, aspect ratio, and reference images are configurable.]

## Skill Version(s):

1.2.42 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
