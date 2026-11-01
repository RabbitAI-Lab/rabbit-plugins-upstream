## Description:

Use dLazy's hosted Qwen 3.8 Max model to generate text from prompts and image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to generate text, work through complex reasoning and code tasks, and analyze long context with dLazy's hosted Qwen model. Image inputs are also supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image files are sent to dLazy's hosted API and media storage.

Mitigation: Only send prompts and images you are comfortable sharing with dLazy, and review its service terms.

Risk: The CLI needs a dLazy API key, and requests may incur usage charges.

Mitigation: Prefer device login or the DLAZY_API_KEY environment variable for credentials, and use --dry-run to review the payload and estimated cost before a request.

## Reference(s):

- [dLazy service information](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [Generated content returned in a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and up to 10 image references; supports asynchronous task IDs and optional file saving.]

## Skill Version(s):

1.2.32 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
