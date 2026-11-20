## Description:

Chat with the dLazy sandbox agent in project-scoped, multi-turn sessions and discover available skills and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill to start or continue project-scoped conversations with dLazy's hosted sandbox agent, optionally selecting a template and attaching files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic activation phrases could route unrelated requests to dLazy; chat messages and attached files are sent to its hosted services.

Mitigation: Review the activation phrases and invoke the skill only when you intend to use dLazy; share only messages and files intended for that service.

Risk: The security review is incomplete because several referenced local items could not be resolved.

Mitigation: Review the unresolved referenced items before relying on the security assessment.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)

## Skill Output:

**Output Type(s):** [Text, Guidance, Code]

**Output Format:** [Streaming conversational text that may include Markdown or task-specific code]

**Output Parameters:** [Multi-turn, project-scoped conversations]

**Other Properties Related to Output:** [Session-based; replies depend on the selected skill or template and user prompt.]

## Skill Version(s):

1.2.45 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
