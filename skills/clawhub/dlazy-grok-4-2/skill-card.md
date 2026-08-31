## Description:

Provides Grok 4.2 text generation, dialogue question answering, and logical reasoning through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to route prompts to dLazy's Grok 4.2 service for text generation, chat-style question answering, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media paths are sent to dLazy's hosted Grok 4.2 service.

Mitigation: Use the skill only when hosted dLazy inference is intended, and avoid submitting sensitive content unless it is appropriate for that service.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Skill use may consume dLazy credits or route ordinary chat requests to the service by accident.

Mitigation: Invoke the skill explicitly for intended Grok 4.2 requests and use dry-run or account checks before high-volume usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [CLI JSON responses and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com; may return asynchronous task metadata when --no-wait is used.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
