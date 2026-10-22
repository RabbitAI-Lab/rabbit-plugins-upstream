## Description:

Helps create e-commerce product images inspired by a reference image's composition and visual style, using the user's own product image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to generate product main-image candidates based on a competitor or popular image's layout and aesthetic while substituting their own product and copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external qhkit package and LinkPix service handle the account token and uploaded product and reference images.

Mitigation: Confirm trust in the package and service before installation or upload, and avoid sharing sensitive images or tokens unnecessarily.

Risk: Unpinned package upgrades or persistent Node PATH changes can alter the runtime environment.

Mitigation: Pin the qhkit version for reproducibility and change shell startup files only when persistence is intended.

Risk: Generated images may inadvertently reproduce another seller's branding or misstate product details.

Mitigation: Request original replacement copy, exclude reference logos and watermarks, and review generated text and product features before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images should be checked for accurate product details, text, and branding.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
