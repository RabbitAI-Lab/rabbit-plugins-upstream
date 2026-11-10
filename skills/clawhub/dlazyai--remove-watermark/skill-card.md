## Description:

Removes watermarks, text, badges, and decorative frames from images and reconstructs the covered areas with an image generation model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Image editors and developers use the skill to remove permitted text and graphic overlays before reusing images or passing them to downstream image workflows. Because covered areas are reconstructed, review the result when visual details or pixel-level fidelity matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because scanners report capabilities beyond its stated image watermark-removal purpose, and some package components were only partially analyzed.

Mitigation: Review the package and its undeclared capabilities before installation or execution; the partial scan does not establish that unexamined content is safe.

Risk: Prompts and image data may be sent to an external image service, and the skill has broader generation capabilities than its stated purpose.

Mitigation: Check the selected provider and its data handling, and use only images whose transmission you accept. Review the requested generation task before execution.

Risk: Reconstructed areas are inferred and may alter obscured content or nearby image details.

Mitigation: Inspect the output and use a pixel-level editing tool when exact preservation is required.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI and data flow reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Edited raster image (JPEG by default) with Markdown command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covered pixels are model-inferred, and other parts of the image may also change slightly; inspect results when fidelity matters.]

## Skill Version(s):

1.0.30 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
