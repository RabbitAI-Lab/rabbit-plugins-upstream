## Description:

Generates ecommerce product detail page images by analyzing a reference detail page and applying a similar layout and visual style to the user's product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agent users use this skill to recreate the layout and visual style of a reference product detail page for their own product images and copy. It supports page-by-page generation, expectation setting for non-pixel-perfect results, and safer replacement of original brand elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if pasted into chat or persisted in CLI configuration.

Mitigation: Configure the qhkit token through a local secret store, environment variable, or trusted configuration UI, and avoid sharing raw keys in conversation.

Risk: Image generation can consume qhkit credits when generate commands run.

Mitigation: Run an estimate first, disclose expected credits and generation parameters, and wait for explicit user approval before submitting a generate command.

Risk: Reference-based detail page generation may unintentionally carry over original brand names, logos, or product identity.

Mitigation: Use the user's own product assets and replacement copy, and keep the constraint that original products, brand names, and logos must not appear in generated outputs.

Risk: The skill produces a generative approximation rather than a pixel-perfect recreation.

Mitigation: Set expectations before generation and review outputs for layout, copy, brand, and compliance issues before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and qhkit credit usage after an approved generation run.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
