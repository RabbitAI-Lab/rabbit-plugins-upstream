## Description:

Helps edit text in product images, including titles, prices, selling points, and promotions, while aiming to preserve the surrounding design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content teams use this skill to revise prices, headlines, and promotional copy in existing product images without redesigning each image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided images are processed by the external qhkit service.

Mitigation: Submit only images suitable for external processing and use a managed environment where needed.

Risk: Installing or updating an unpinned npm CLI may change the local toolchain.

Mitigation: Prefer a reviewed, pinned qhkit version or a managed environment.

Risk: Generative edits may alter prices, wording, logos, or product details.

Mitigation: Inspect each output and verify text, prices, logos, and product details before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown with CLI commands, image links, and brief usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent and calls for visual verification of generated images.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
