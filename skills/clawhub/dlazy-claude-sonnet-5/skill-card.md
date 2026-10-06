## Description:

Helps agents use dLazy's hosted Claude Sonnet 5 service for text and code generation from prompts, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to submit prompts and optional images or videos to dLazy's hosted service for generated text, code, and reasoning assistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media are sent to dLazy's cloud service.

Mitigation: Review inputs for sensitive information before submitting them.

Risk: Authentication may save an API key in local CLI configuration.

Mitigation: Protect the local configuration and use a per-invocation key when persistent storage is undesirable.

Risk: Using the skill installs or runs a third-party CLI.

Mitigation: Review the CLI source and package; prefer the pinned on-demand invocation if a persistent global binary is not wanted.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier instead of immediate content.]

## Skill Version(s):

1.2.27 (source: ClawHub release; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
