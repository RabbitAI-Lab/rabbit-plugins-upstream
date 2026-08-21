## Description:

Generates e-commerce promotional posters and discount marketing images for product launches, seasonal campaigns, and brand promotion using LinkPix qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through creating promotional e-commerce poster images with optional product references, model and size selection, credit estimation, user confirmation, and qhkit delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit globally or install Node, changing persistent host tooling.

Mitigation: Review install and upgrade commands before execution, and prefer an isolated environment or npx fallback when global changes are not intended.

Risk: The skill uploads prompts and product images to an external Qinghu/LinkPix service and consumes API credits.

Mitigation: Confirm model, size, reference images, estimated credits, and content sensitivity with the user before generation.

Risk: The skill may reuse an existing root-owned Qinghu token if present.

Mitigation: Run it only where that token is authorized for this workflow, and verify the account and token scope before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide qhkit image-generation submissions that return image URLs; credit-consuming generation requires user confirmation before submission.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
