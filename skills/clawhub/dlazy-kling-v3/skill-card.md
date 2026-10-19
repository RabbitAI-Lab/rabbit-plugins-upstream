## Description:

Helps agents generate Kling V3 videos from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent to generate videos from text or reference images with Kling V3 via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's cloud service, where generated results are hosted.

Mitigation: Send only media and prompts you are comfortable sharing with dLazy; review its service terms before use.

Risk: API calls may consume paid credits.

Mitigation: Check the cost estimate with dry-run before generating when cost matters.

Risk: Authentication can store an API key in the local dLazy configuration.

Mitigation: Protect access to the local configuration and rotate or revoke the key if needed.

Risk: The skill invokes a third-party CLI package.

Mitigation: Review the pinned npm package and linked CLI source before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Text and shell commands; the CLI returns JSON with hosted media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can download a generated result to a local path when requested.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
