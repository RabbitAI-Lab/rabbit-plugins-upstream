## Description:

Provides Grok 4.2 text generation, dialogue question answering, and logical reasoning through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke Grok 4.2 through dLazy for text generation, chat-style Q&A, and reasoning tasks from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly supplied local media files may be sent to dLazy hosted services.

Mitigation: Avoid sending sensitive content unless third-party processing is acceptable for the task and account.

Risk: Broad chat and Q&A triggers can lead to unintended invocation of a third-party model service.

Mitigation: Use explicit Grok or dLazy invocation when calling the skill and confirm user intent before sending sensitive prompts.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate, rotate or revoke saved keys as needed, and restrict access to the local config file.

Risk: Installing a global npm CLI adds third-party executable code to the user's environment.

Mitigation: Review the npm package or source before global installation, or prefer the pinned npx invocation for one-off use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Text or JSON returned by the dLazy CLI, usually summarized or presented as Markdown by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and explicitly supplied media files are handled by dLazy hosted endpoints.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
