## Description:

Logo 设计 Logo Design helps users create, upgrade, or evaluate logo and brand identity concepts with transparent-background logo output and multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and brand teams use this skill to delegate logo and visual-identity work to the dLazy hosted logo-design agent, including concept generation, refinement, evaluation, and multi-turn project continuation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and attached files to the external dLazy service.

Mitigation: Use it only with data appropriate for dLazy, and attach only files intended for upload.

Risk: Global installation of the third-party CLI persists a local executable and API-key configuration.

Mitigation: Prefer the pinned npx invocation or an isolated environment when possible, and use a revocable API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and SaaS agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded user-provided files and project-scoped chat sessions handled by the dLazy CLI.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
