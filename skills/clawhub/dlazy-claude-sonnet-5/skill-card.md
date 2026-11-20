## Description:

Provides a CLI interface for sending prompts and optional image or video inputs to dLazy's hosted Claude Sonnet 5 service and receiving generated results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to send prompts and optional image or video inputs to dLazy's hosted generation service through its CLI. It returns generated content, including text or structured results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted a mismatch between advertised model capabilities and CLI authentication commands, and some referenced material was unavailable.

Mitigation: Review the skill instructions and the dLazy CLI's behavior, and confirm the advertised capabilities before installing or providing credentials.

Risk: Prompts and supplied local media are sent to dLazy's hosted service; the CLI stores an API key in the user's configuration or accepts it through an environment variable.

Mitigation: Avoid sending sensitive content unless approved for the service, protect the CLI configuration and environment, and rotate or revoke keys when needed.

## Reference(s):

- [Skill release page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [Generated text or structured JSON returned through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts prompts and optional image or video inputs; results may be asynchronous.]

## Skill Version(s):

1.2.45 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
