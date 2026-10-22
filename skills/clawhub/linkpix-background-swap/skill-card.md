## Description:

Helps users replace product photo backgrounds with generated marketing scenes using LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketers use this skill to place product photos into new promotional scenes and produce multiple background variations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and an account token are used with the LinkPix/qhkit service.

Mitigation: Use only images approved for upload, keep the API token private, and install only if this provider is acceptable.

Risk: Image generation consumes account credits and can change product details, including text and logos.

Mitigation: Check the credit estimate before generation and review each resulting image against the original product.

Risk: Installing or updating the qhkit dependency can change the executable used by the skill.

Mitigation: Use a pinned or reviewed qhkit version in managed environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with generated image links and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image links are provided after completion; credit charges are reported.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
