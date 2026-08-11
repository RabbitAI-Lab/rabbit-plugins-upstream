## Description:

Chat with the dLazy sandbox agent, a project-scoped assistant that runs skills end-to-end over multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped, multi-turn conversations with the dLazy sandbox agent, including template selection, file attachment, and chat session management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases could route ordinary chat requests to the third-party hosted dLazy service unexpectedly.

Mitigation: Use explicit invocations such as dlazy chat or dLazy sandbox agent, especially when a prompt may contain sensitive context.

Risk: Prompts and attached files may be sent to dLazy-hosted API and file endpoints.

Mitigation: Avoid sending sensitive prompts or attachments unless they are approved for dLazy, and rotate or revoke API keys when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Streaming terminal text, often formatted as Markdown with inline commands or code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped chat sessions and user-attached files handled by the dLazy CLI.]

## Skill Version(s):

1.2.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
