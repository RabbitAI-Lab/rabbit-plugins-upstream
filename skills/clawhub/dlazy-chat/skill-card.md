## Description:

Chat with the dlazy sandbox agent, a project-scoped assistant that runs skills end-to-end over multiple turns and discovers available skills and projects through the dlazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped, multi-turn conversations with the dLazy hosted sandbox agent. It is suited for conversational workflows where the agent may run selected skills or templates and maintain project context across turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected project context, and files passed with --files are sent to the dLazy hosted service.

Mitigation: Use the skill only when hosted processing is intended, and avoid sending sensitive files or prompts unless the target organization permits that use.

Risk: The skill requires a dLazy API key stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the local CLI configuration, prefer per-invocation environment variables on shared systems, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped chat state and uploaded file URLs managed by the dLazy hosted service.]

## Skill Version(s):

1.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
