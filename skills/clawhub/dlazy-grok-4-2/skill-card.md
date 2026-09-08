## Description:

Provides text generation, dialogue QA, and logical reasoning through the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to send prompts to the dLazy Grok 4.2 CLI for text generation, chat-style question answering, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files supplied to the CLI may be sent to dLazy hosted API and media storage endpoints.

Mitigation: Avoid sending sensitive prompts or files unless intended, and review dLazy service handling before use.

Risk: Using the global install path leaves a persistent third-party CLI binary on the system.

Mitigation: Prefer the pinned npx invocation for on-demand use when a persistent global binary is not needed.

Risk: Authentication stores a dLazy API key in the local CLI configuration.

Mitigation: Protect the local user config, use the environment variable path for per-invocation secrets when appropriate, and rotate or revoke keys from the dLazy dashboard if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain text with optional JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and file endpoints.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
