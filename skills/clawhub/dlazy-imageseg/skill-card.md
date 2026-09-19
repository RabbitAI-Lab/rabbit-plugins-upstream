## Description:

Image matting skill that separates foreground from background and returns a transparent-background image URL for product images, character cutouts, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy image segmentation for foreground/background separation and receive transparent-background image URLs for product imagery, cutouts, and compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided media paths may be uploaded to dLazy's hosted service, and generated outputs are hosted by dLazy.

Mitigation: Use the skill only with media that is appropriate to send to dLazy's cloud service; review service terms and data handling before processing sensitive assets.

Risk: Authentication stores a dLazy API key in the local CLI configuration when the user logs in.

Mitigation: Prefer per-invocation credentials or rotate and revoke the API key from the dLazy dashboard when access is no longer needed.

Risk: The artifact documentation conflicts on the primary image argument, while security guidance notes the imageseg argument should be verified.

Mitigation: Run dlazy imageseg -h before execution and use the current documented image option from the installed pinned CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs from files.dlazy.com; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
