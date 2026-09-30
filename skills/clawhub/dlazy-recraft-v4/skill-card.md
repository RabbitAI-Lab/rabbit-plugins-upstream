## Description:

Generates 1MP raster images with Recraft V4 for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate 1MP images from text prompts for creative work and quick design iterations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the third-party dLazy CLI requires trusting its npm package.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package and its source before installation.

Risk: Saved dLazy API keys persist in local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY if persistent credential storage is undesirable.

Risk: Prompts and explicitly supplied files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files unless their transfer to dLazy is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [CLI instructions and JSON results with image URLs]

**Output Parameters:** [1D; text prompt and optional aspect ratio]

**Other Properties Related to Output:** [Generated images can be saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
