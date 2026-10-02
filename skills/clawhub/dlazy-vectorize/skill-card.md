## Description:

Helps agents convert raster images into scalable vector artwork using dLazy's hosted vectorization service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to turn PNG or JPG images, such as logos and icons, into vector artwork and obtain a result URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images and request data are sent to dLazy's hosted service.

Mitigation: Only submit images and data you are comfortable uploading to a third party.

Risk: Logging in can save the dLazy API key in a local CLI configuration file.

Mitigation: Use a per-invocation DLAZY_API_KEY when you do not want the key saved locally; rotate or revoke exposed keys.

Risk: Using the third-party npm CLI executes vendor-provided code.

Mitigation: Review the CLI before installing; use the documented pinned npx invocation if you prefer not to install it globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and JSON result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns a result URL; the CLI can optionally save the generated asset locally.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
