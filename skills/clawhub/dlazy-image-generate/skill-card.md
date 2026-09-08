## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to route image-generation, image-editing, upscaling, matting, and vectorization requests through the dLazy CLI and hosted image APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local input files can be sent to dLazy's hosted service for generation.

Mitigation: Avoid passing private or sensitive files unless the user intends to share them with dLazy.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use revocable credentials and rotate or revoke the key when access is no longer needed.

Risk: Generated outputs are hosted by dLazy and returned as hosted URLs.

Mitigation: Treat output URLs as externally hosted artifacts and avoid including confidential content in generation requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands; dLazy CLI invocations return JSON envelopes and hosted output URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image, SVG, matting, upscaling, and related media outputs are returned through dLazy-hosted URLs.]

## Skill Version(s):

1.3.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
