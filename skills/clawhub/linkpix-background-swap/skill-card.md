## Description:

Uses the qhkit CLI to replace ecommerce product image backgrounds while preserving the product subject and generating marketing-scene variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to turn product photos into scene-based marketing images by asking an agent to invoke qhkit background replacement. It is intended for product background swaps, white-background-to-scene edits, and multiple scene variants of the same product image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images provided to the skill may be uploaded to the third-party qhkit service.

Mitigation: Use the skill only when the user is comfortable with that upload path, and avoid submitting sensitive or restricted images.

Risk: The qhkit CLI may use an existing OpenClaw qinghu token or a token configured by the user.

Mitigation: Confirm the intended token source, keep tokens out of chat transcripts and logs, and use the configured qhkit mechanisms for credential storage.

Risk: Ambiguous image-editing requests could be treated as background replacement when another edit type was intended.

Mitigation: Confirm background replacement intent before invoking qhkit for ambiguous requests.

Risk: Generative background replacement can slightly change product details such as text, logos, or structure.

Mitigation: Review generated images before delivery or publication, with extra attention to brand marks, text, and product geometry.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and actual qhkit credit usage when the CLI generation command completes.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
