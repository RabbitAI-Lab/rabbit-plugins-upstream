## Description:

Generates macro clothing detail images from garment photos for e-commerce pages, focusing on fabric texture, stitching, weave structure, trims, and construction details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and developers use this skill to turn standard clothing product images into focused macro detail shots for e-commerce listings. It helps prepare prompts, provider calls, and saved image outputs while preserving visible garment color, stitch pattern, and construction details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and garment images may be sent to dLazy or another configured image provider.

Mitigation: Use only local image files or trusted public image URLs, and avoid confidential product assets, customer data, credentials, and private intranet URLs unless that provider use is approved.

Risk: Generated files are saved locally and may contain inaccurate or invented garment details when the source image is low resolution, compressed, or obstructed.

Mitigation: Start from clear source images, generate one detail area per prompt, and review outputs for texture realism, color consistency, and construction details before publication.

## Reference(s):

- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, prompt text, configuration examples, and image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides generation of local JPEG image files through dLazy or another configured image provider.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
