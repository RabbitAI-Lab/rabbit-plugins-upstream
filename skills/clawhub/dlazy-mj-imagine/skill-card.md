## Description:

Helps create stylized images through dLazy's Midjourney-style generation service, with aspect ratio, bot type, and grid or selected-image options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request artistic images with a prompt and select aspect ratio, bot type, and grid or individual-image output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI requires trusting its publisher and package.

Mitigation: Confirm you trust dLazy and the pinned @dlazy/cli package before installing.

Risk: Prompts and any media files supplied to the CLI may be sent to dLazy-hosted services; generated results are hosted remotely.

Mitigation: Avoid submitting sensitive prompts or media, and review the service terms before use.

Risk: Signing in or saving an API key persists credentials locally.

Mitigation: Use DLAZY_API_KEY per invocation if local key storage is not desired.

## Reference(s):

- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text or Markdown with commands and image-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns image URLs; asynchronous requests can return a task ID for later status checks.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
