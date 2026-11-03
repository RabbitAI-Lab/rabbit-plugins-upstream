## Description:

Chat with dLazy’s project-scoped sandbox agent across multiple turns, discovering skills and projects as needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and dLazy users use this skill to start or continue project-scoped, multi-turn conversations with the hosted dLazy agent, including work with selected skill templates and optional file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases could send ordinary conversations to dLazy without a deliberate choice.

Mitigation: Require the user to explicitly select dLazy before invoking the skill.

Risk: Prompts and selected attachments are sent to dLazy, and tasks may consume credits.

Mitigation: Tell users what they are sending, avoid sharing sensitive content, and check expected credit use before starting a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Streaming conversational response, with Markdown when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response content depends on the selected task.]

## Skill Version(s):

1.2.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
