## Description:

Provides access to the dLazy hosted Qwen 3.8 Max generation service for text prompts and optional image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users submit text prompts and optional images to dLazy's hosted Qwen 3.8 Max service, then retrieve generated results through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied skill content does not demonstrate the advertised Qwen model capabilities.

Mitigation: Verify the model identity and expected capabilities with the service provider before relying on results.

Risk: The behavior of the referenced CLI package was not established by the security scan.

Mitigation: Review the CLI package and its permissions before installation, and use the pinned version specified by the skill.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON response containing generated results; optional downloadable asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result content varies by prompt; asynchronous requests may first return a task ID.]

## Skill Version(s):

1.2.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
