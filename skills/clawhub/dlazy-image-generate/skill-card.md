## Description:

Selects a dLazy CLI image model for generating or editing images from user prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run dLazy image-generation, editing, or enhancement models for visual assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy, and generated files are hosted there.

Mitigation: Avoid private prompts or media unless you intend to share them with dLazy.

Risk: Logging in may save an API key in the user's local CLI configuration.

Mitigation: Protect the user configuration and rotate or revoke the key if exposed.

Risk: Hosted generation may consume paid credits; installing the external CLI globally persists a local binary.

Mitigation: Check credit usage and use the documented pinned npx invocation if a global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Text and shell commands; CLI responses are JSON with generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted by dLazy; model selection depends on the requested task.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
