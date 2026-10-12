## Description:

The release listing describes creating social-style outfit images with new models and scenes, while the supplied skill instructions instead describe extracting clothing into white-background flat-lay images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Retailers and content creators can use the listed skill to create social-style outfit images from clothing photos; confirm the intended workflow first because the supplied instructions describe garment extraction instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and clothing or model images are sent to the selected cloud image-generation provider.

Mitigation: Use only images you are comfortable sharing with that provider; prefer local images or trusted public URLs and avoid private or internal URLs.

Risk: Provider credentials and output files may be exposed or written to an unintended location if settings are not checked.

Mitigation: Review provider credentials in the environment and choose the output path deliberately before running.

Risk: The packaged skill instructions describe a different task from the release listing.

Mitigation: Confirm the intended task and review the packaged instructions before generating images.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider setup and data flow](artifact/references/provider-cli.md)
- [Image model parameters](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [JPEG image files with text guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The release listing describes lifestyle outfit images, but the supplied SKILL.md documents flat-lay garment images; verify the release contents before use.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
