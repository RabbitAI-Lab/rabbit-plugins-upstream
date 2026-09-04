## Description:

Generate exquisite images with Kling o1 model, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to ask an agent to generate or edit images through the dLazy Kling Image O1 command-line workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a suspicious verdict because the skill's API key storage claim is stronger than what the inspected CLI package enforces.

Mitigation: Prefer per-invocation DLAZY_API_KEY or manually restrict ~/.dlazy/config.json permissions on shared systems.

Risk: Prompts and selected reference files are sent to dLazy services for generation.

Mitigation: Avoid sending confidential prompts or files unless that data sharing is acceptable for the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return generated image URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
