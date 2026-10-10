## Description:

Guides agents in generating digital-human broadcast videos from a portrait and audio or text using Jimeng OmniHuman 1.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through creating digital-human presenter videos from a portrait and audio or a text prompt with dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the third-party CLI executes software on the user's system.

Mitigation: Review the pinned @dlazy/cli package before installing or running it.

Risk: A dLazy API key is needed to use the hosted service.

Mitigation: Store or pass the key only through the documented authentication methods and rotate it if exposed.

Risk: Submitted portraits and audio are uploaded to dLazy's hosted service.

Mitigation: Only provide media files you intend to send to dLazy.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return a hosted media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
