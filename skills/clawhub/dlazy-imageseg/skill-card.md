## Description:

Separates an image's foreground from its background and returns a transparent-background result URL for product photos, portraits, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to remove image backgrounds for product imagery, portrait cutouts, and compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images are sent to dLazy's hosted service.

Mitigation: Send only images you are authorized to share with that service.

Risk: A dLazy API key may be saved locally for authentication.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: An example uses --prompt despite the documented --image option.

Mitigation: Check dlazy imageseg -h and use the supported image-input syntax before running a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with a hosted transparent-image URL; asynchronous requests can return a task ID, and --save can download the image.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
