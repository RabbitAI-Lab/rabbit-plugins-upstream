## Description:

Efficient text generation, dialogue QA, and logical reasoning using the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask questions, generate prose, and perform logical reasoning through the dLazy-hosted Grok 4.2 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the text-chat description does not match image/media behavior, and selected local media paths may be sent to dLazy.

Mitigation: Use this skill only when dLazy CLI calls and any selected media uploads are intended, and avoid passing sensitive prompts or file paths unless approved.

Risk: The security review says broad triggers could send ordinary prompts to a paid third-party API.

Mitigation: Confirm the user intends to use dLazy/Grok 4.2 before invoking the CLI, and use dry-run or cost-estimate behavior when cost sensitivity is unclear.

Risk: The skill requires storing or passing a dLazy API key that may consume credits.

Mitigation: Store credentials using the documented dLazy authentication flow, rotate or revoke keys when needed, and notify users when authorization or insufficient-credit errors occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI homepage from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package from metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage from metadata](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [CLI JSON responses and generated text returned through the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and selected local media paths may be sent to dLazy endpoints.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
