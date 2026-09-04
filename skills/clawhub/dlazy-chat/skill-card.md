## Description:

沙箱智能体对话 Chat lets agents use dLazy's project-scoped sandbox chat to run multi-turn work and continue projects through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped, multi-turn conversations with the dLazy sandbox agent and to run selected skills through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy's hosted service.

Mitigation: Use the skill only when hosted dLazy processing is intended, and avoid attaching sensitive files unless that transfer is acceptable.

Risk: Authentication may save an API key in local CLI configuration.

Mitigation: Use per-run environment variables where appropriate, or verify local config permissions on shared machines.

Risk: Generic chat requests could activate this skill unintentionally.

Mitigation: Invoke it only when the user clearly intends to use dLazy chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Terminal chat output and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the dLazy hosted service and may reference uploaded user-selected files.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
