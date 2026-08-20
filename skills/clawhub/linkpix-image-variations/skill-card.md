## Description:

Uses the qhkit CLI package @iqinghu/qhkit to generate multiple e-commerce marketing variants from one product image, with different backgrounds, layouts, and design styles for ad production and A/B testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers, designers, and agent users use this skill to turn a source product image into multiple LinkPix/qhkit marketing image variants for campaign rotation, platform-specific creative sets, and A/B testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and runs qhkit, and sends input product images to the LinkPix/qhkit service.

Mitigation: Confirm the user is comfortable with qhkit installation and image upload before running generation commands.

Risk: Image generation consumes service credits, especially for large batches.

Mitigation: Run the documented qhkit estimate step before submitting large jobs and report insufficient balance before generation.

Risk: Generated redraws can change product details such as text, logos, or structure.

Mitigation: Review generated outputs for key product details before using the assets in marketing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and generated image URLs or CLI JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit estimate results, generation credits consumed, and generated image URLs returned by the CLI.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
