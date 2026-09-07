## Description:

Generates e-commerce macro detail shots from clothing images, focusing on fabric texture, stitching, weave, and construction close-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, e-commerce operators, and developers use this skill to turn ordinary garment product images into detail-page close-ups of collars, cuffs, hems, buttons, zippers, embroidery, prints, weave structures, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and generated outputs may be sent to the selected image provider.

Mitigation: Use only providers and endpoints approved for the image data, and avoid sending sensitive or restricted product media.

Risk: A custom Ark endpoint can expose images or credentials if ARK_BASE_URL points to an untrusted service.

Mitigation: Leave ARK_BASE_URL unset unless the endpoint is explicitly trusted and credential handling has been reviewed.

Risk: The bundled shared task list includes a remove-watermark task unrelated to clothing detail generation.

Mitigation: Run only the clothing-detail task for this release and do not use watermark removal on third-party or rights-restricted media.

Risk: Unpinned global CLI installs can change behavior between runs.

Mitigation: Prefer pinned or local CLI execution, and review command output with --dry-run before paid generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and saved JPEG image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are typically JPEG outputs; the clothing-detail task defaults to high quality at 1024x1024, with optional 1024x1536 vertical detail-page output.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
