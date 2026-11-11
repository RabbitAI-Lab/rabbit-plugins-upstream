## Description:

Extracts a garment from a photo and produces a clean, white-background e-commerce flat-lay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content creators use this skill to turn a model, street-style, or customer photo into a clean product flat-lay for a listing or as input to related garment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos may be sent to external image services; ClawScan reports incomplete inspection of some artifact components.

Mitigation: Before use, check which service receives the images and review its data handling terms; confirm you are comfortable sending the photos there.

## Reference(s):

- [Model flags reference](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Prompt text, Guidance]

**Output Format:** [JPEG or PNG images with Markdown guidance, prompt templates, and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Occluded garment details may be inferred; results depend on source image quality and visibility.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
