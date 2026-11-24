## Description:

Removes watermarks, text, badges, and decorative overlays from images by reconstructing the covered areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can prepare images for downstream image workflows by removing text and other overlays. The skill is intended for image cleanup where reconstructed areas can be reviewed afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a medium-confidence suspicious verdict, broader generation features beyond the stated purpose, an external image-provider workflow, and partially analyzed content.

Mitigation: Review the skill's capabilities and provider data handling before use, and proceed only if its broader features and possible transfer of image or prompt data are acceptable.

Risk: Reconstructed areas are inferred by a model, and other parts of the image may also be slightly redrawn.

Mitigation: Inspect the result manually; use a professional pixel-editing tool when exact pixel preservation is required.

Risk: Removing copyright watermarks, brand marks, or required labels can misrepresent image ownership or product information.

Mitigation: Only edit images you are authorized to change, and do not remove marks to misrepresent ownership, branding, or required product information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Model flags reference](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Edited image files (JPEG, PNG, or WebP), with Markdown guidance and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed image regions are model-inferred; the scene may be slightly redrawn beyond the covered areas.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
