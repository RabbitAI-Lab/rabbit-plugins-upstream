## Description:

Enhances low-resolution images with dLazy's cloud super-resolution service and returns an upscaled image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upscale low-resolution images through the dLazy CLI and retrieve enhanced image URLs for restoration or downstream asset workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy's cloud service for processing.

Mitigation: Use dry-run or explicit confirmation before uploading private media, and avoid sending sensitive images unless the user accepts the cloud-processing risk.

Risk: The dLazy CLI requires an API key that may be stored in local configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx when less local persistence is desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Install only when the user trusts dLazy, keep the pinned CLI version under review, and treat service errors or insufficient-credit responses as user-actionable conditions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an enhanced image URL; asynchronous requests may return a task ID for polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
