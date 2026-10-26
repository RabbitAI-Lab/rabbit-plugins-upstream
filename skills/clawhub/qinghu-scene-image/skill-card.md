## Description:

Generates product lifestyle scene images from a supplied product photo using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and marketers use the skill to generate single or grouped product-in-context images for product pages and advertising.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating external tools globally, fetching Node binaries, and changing shell PATH can affect the user's environment.

Mitigation: Review installation steps first; prefer a pinned, preinstalled qhkit in a contained environment and avoid persistent PATH changes.

Risk: Product images may be uploaded to Qinghu services for generation.

Mitigation: Confirm the user permits uploading the images before sending them to the service.

Risk: A token for the wrong account or site can expose credentials to an unintended service.

Mitigation: Provide tokens only for the intended account and site, and verify the selected site before use.

Risk: Generative redraws can alter product text, logos, or structure.

Mitigation: Review generated images against the original product before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown with command examples and generated-image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return multiple images and report the credits charged; generated product details should be checked.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
