## Description:

Uses the dLazy-hosted Grok 4.2 model for text generation, conversational questions, and reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to generate text, answer questions, and work through reasoning tasks using dLazy's hosted model service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media paths passed to the tool may be sent to dLazy's hosted service.

Mitigation: Review prompts and file paths before invoking the skill; avoid sending sensitive material without authorization.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the local configuration or supply the key per invocation, and rotate the key if exposed.

Risk: Broad chat or question-answering triggers can route requests to an external paid API.

Mitigation: Invoke the dLazy/Grok command explicitly and check expected costs before making calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI project (release metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Natural-language text delivered through a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of generated output.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
