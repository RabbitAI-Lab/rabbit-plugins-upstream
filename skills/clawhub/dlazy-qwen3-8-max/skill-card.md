## Description:

Helps agents use dLazy's hosted Qwen model for reasoning, coding, and analysis of text or images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to generate text, reason through complex questions, write code, or analyze text and images through dLazy's hosted Qwen service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive information before submitting them.

Risk: The third-party CLI can persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if you do not want to save the key locally.

Risk: A global CLI installation persists a third-party executable.

Mitigation: Use the pinned npx invocation if you prefer not to install a global binary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Analysis]

**Output Format:** [Generated content returned in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of immediate content.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
