## Description:

Helps an agent replace the product subject in an ecommerce scene image with a new product while preserving the scene, composition, perspective, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, merchants, and ecommerce content teams use this skill to reuse existing product-scene imagery for new products. The agent prepares qhkit image-generation commands, checks model and size options, estimates credits, asks for confirmation before paid generation, and returns generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and uses the qhkit package/provider.

Mitigation: Install only when the user trusts qhkit and the provider, and verify the package, model, image count, size, and requested files before generation.

Risk: Referenced images may be uploaded to the image-generation provider.

Mitigation: Tell users which local or remote images will be used and avoid uploading sensitive or unauthorized product images.

Risk: Generation can spend credits after task submission.

Mitigation: Run an estimate when supported, report the expected credit cost, and wait for explicit user approval before running generate.

Risk: Generated product replacements may differ slightly from the source product.

Mitigation: Review outputs for product structure, logos, text, perspective, reflections, and other business-critical visual details before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command parameters, credit estimates, confirmation text, and generated image URLs when execution is approved.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
