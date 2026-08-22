## Description:

LinkPix helps agents edit target text in ecommerce product images, such as titles, prices, selling points, and promotional copy, while preserving the rest of the image as much as the image generation workflow allows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to ask an agent to update visible text in product images, including prices, titles, sales copy, and promotional details. The skill guides the agent through qhkit image generation, option checks, cost estimation, user confirmation, result review, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can install or upgrade global Node and qhkit tooling.

Mitigation: Review installation commands before use and run the skill only in an environment where global tooling changes are acceptable.

Risk: The workflow can reuse an existing OpenClaw qhkit token.

Mitigation: Confirm that token reuse is authorized for the current environment before running qhkit commands.

Risk: Local product images may be uploaded to the provider during qhkit image generation.

Mitigation: Use only images that are approved for upload to the provider and avoid sensitive or restricted product imagery.

Risk: Generated edits are not pixel-level repairs and may alter non-target image details.

Mitigation: Inspect generated images before delivery, especially prices, spelling, logos, and product structure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline bash commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may return generated image URLs and qhkit credit usage after a confirmed generation task completes.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
