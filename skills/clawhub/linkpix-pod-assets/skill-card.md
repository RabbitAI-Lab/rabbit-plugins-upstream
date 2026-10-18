## Description:

Helps print-on-demand sellers extract print artwork, create design variations, and preview designs on products using LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Print-on-demand sellers and ecommerce designers use this skill to extract print designs, generate variations, and preview artwork on merchandise before listing it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing qhkit or Node and changing PATH alters the local environment.

Mitigation: Approve installation and configuration changes deliberately; prefer a pinned qhkit version where possible.

Risk: Local images sent to qhkit are uploaded to the provider, and generation may consume account credits.

Mitigation: Confirm image-sharing and credit use before submission; review the estimated credits.

Risk: Generated artwork may differ from the source design or include protected third-party artwork.

Mitigation: Review key visual details and confirm rights to source artwork before commercial use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image URLs, Guidance]

**Output Format:** [Markdown with command examples and generated-image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual account credits used when images are generated.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
