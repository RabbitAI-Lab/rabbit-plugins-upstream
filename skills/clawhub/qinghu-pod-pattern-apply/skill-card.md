## Description:

Helps create realistic product mockups by applying a supplied print design to clothing, hats, mugs, and other merchandise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and designers use this skill to preview print-on-demand designs on apparel and other products before listing or presenting them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and a service token are provided to an external image-generation service.

Mitigation: Use only images approved for external upload and handle the API token as a secret.

Risk: Installing or upgrading qhkit may modify local Node/npm tooling.

Mitigation: Review installation changes and prefer an existing or pinned qhkit version when possible.

Risk: Generated mockups may alter fine details or colors of the supplied design.

Mitigation: Check the finished images against the original design before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-pod-pattern-apply)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown text with command examples and links to generated mockups]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the actual credits used when an image is generated.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
