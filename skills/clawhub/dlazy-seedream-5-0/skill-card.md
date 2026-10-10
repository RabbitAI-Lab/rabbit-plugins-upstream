## Description:

Generates 2K, 3K, or 4K images from prompts and reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution visuals and rework reference images for posters, key visuals, and print.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference media may be sent to dLazy's hosted service.

Mitigation: Avoid sensitive prompts and local files unless their upload is approved.

Risk: Login stores an API key in the local CLI configuration.

Mitigation: Protect access to the local configuration and rotate or revoke the key if exposed.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the CLI source and package before installation; use the pinned on-demand package when a global install is not needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI source link (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [CLI commands and JSON results containing generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K generation, up to 10 reference images, and optional local saving.]

## Skill Version(s):

1.2.23 (source: ClawHub release; skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
