## Description:

LinkPix helps agents edit targeted text in ecommerce product images, such as titles, prices, selling points, and promotion copy, while preserving the rest of the image as much as possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agents use this skill to update text in product images, including price changes, title revisions, selling-point updates, and campaign copy refreshes. It is intended for assisted image-editing workflows where the user reviews generated results before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to an external image-generation service through the qhkit CLI.

Mitigation: Avoid highly sensitive images and use an appropriate API key for the task.

Risk: Image generation can consume paid credits.

Mitigation: Run an estimate when supported and obtain explicit user confirmation for model, image count, size, reference images, and expected credit cost before generation.

Risk: Generated edits may alter non-text details or produce incorrect text, numbers, logos, or product structure.

Mitigation: Visually inspect each generated image and rerun with more precise instructions before delivery when critical details are wrong.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs through qhkit; paid generation requires explicit user confirmation before submission.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
