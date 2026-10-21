## Description:

Upscales low-resolution images through the dLazy service and returns a URL for the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to enhance low-resolution images and obtain links to the upscaled results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images supplied to the service are uploaded to dLazy cloud storage.

Mitigation: Only submit images you are authorized to share with dLazy.

Risk: Logging in can save an API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY if local key persistence is undesirable.

Risk: The skill relies on the third-party dLazy CLI package and hosted service.

Mitigation: Confirm you trust the package and service before installing or using them; use npx for on-demand execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return an enhanced image URL or an asynchronous task ID; an optional flag saves the image locally.]

## Skill Version(s):

1.3.33 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
