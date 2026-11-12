## Description:

Analyzes a reference image’s composition, colors, lighting, and style, then creates a prompt for generating a similar image with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can provide a reference image and use the skill to create a new image with a similar visual style through dLazy’s Seedream 4.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and flagged login and API-key setup that should be understood before use.

Mitigation: Review the linked CLI project and the authentication steps before installing or configuring the CLI; use an API key you can rotate or revoke.

Risk: The skill sends prompts to dLazy’s hosted API and uploads supplied local media files to its media storage.

Mitigation: Avoid submitting sensitive images or prompts, and use only content you are permitted to send to the service.

## Reference(s):

- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image, JSON]

**Output Format:** [JSON result containing generated image output and its URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may return an asynchronous task identifier when invoked without waiting for completion.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
