## Description:

Chat with the dlazy sandbox agent, a project-scoped assistant that runs skills end-to-end over multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover dLazy project skills and hold multi-turn conversations with a hosted sandbox agent. It supports starting or continuing project-scoped work and attaching files for the agent to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic chat requests may activate commands that send messages to dLazy or create paid projects without clear user intent.

Mitigation: Activate only for explicit dLazy requests or an established dLazy session, and confirm the intended project before execution.

Risk: Messages and attached files are sent to dLazy; projects may consume credits, and login stores an organization API key locally.

Mitigation: Confirm the prompt and attachments before sending, review credit use, and protect or rotate the locally stored API key as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, API Calls]

**Output Format:** [Streaming text responses in a CLI chat session]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the selected skill and project context; attached files are uploaded to dLazy storage.]

## Skill Version(s):

1.2.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
