## Description:

Chat with the dLazy sandbox agent in project-scoped, multi-turn sessions and discover available skills and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue project-based conversations with the dLazy hosted sandbox agent, discover available skills and projects, and manage multi-turn sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic activation phrases may route ordinary requests to dLazy's external chat service without clear intent; messages and attached files are sent to that service.

Mitigation: Invoke the skill only for explicit dLazy chat requests, review its instructions and linked install details before use, and attach files only when you intend to upload them.

## Reference(s):

- [dLazy CLI source repository (listed by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Conversational text and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses come from a hosted agent; attached files are uploaded to the service.]

## Skill Version(s):

1.2.46 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
