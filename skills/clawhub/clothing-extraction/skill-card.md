## Description:

Extracts clean e-commerce flat-lay clothing images from arbitrary photos, such as model, street-style, buyer-show, or competitor reference images, by keeping the target garment and removing people, props, and backgrounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, designers, and content operators use this skill to turn model, street-style, buyer-show, or competitor reference photos into clean white-background flat-lay clothing product images. Developers can use the included CLI guidance to run the workflow with local files or trusted image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and clothing images may be sent to the selected cloud provider during generation.

Mitigation: Use local input files or trusted image URLs, choose the intended provider deliberately, and run dry-run checks before paid generation when practical.

Risk: Occluded clothing details can be inferred rather than faithfully recovered.

Mitigation: Review generated outputs before use, especially when key garment details were blocked in the source image.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI Reference](references/provider-cli.md)
- [Model Flags Reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with prompt templates and shell command examples; generated image files are saved by the commands when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented workflow uses one input image per extraction, 1024x1024 outputs, high quality settings, and optional batch generation for review.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
