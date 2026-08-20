## Description:

Uses the qhkit CLI to analyze a reference ecommerce product-detail page and generate product-detail images for the user's product with a similar layout and visual style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and designers use this skill to create product-detail page images by matching the layout and visual style of a provided reference page while replacing the product and copy with their own materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to install or upgrade qhkit and Node tooling in the execution environment.

Mitigation: Review installation steps before use and prefer administrator-managed or otherwise trusted dependency installation workflows.

Risk: The workflow uploads product and reference images through qhkit for generation.

Mitigation: Use only images that are approved for upload to the configured service and avoid submitting sensitive or restricted product materials.

Risk: The workflow can rely on configured Qinghu or OpenClaw credentials.

Mitigation: Do not expose API tokens in prompts, logs, command output, or shared artifacts; use environment or configuration storage with appropriate access controls.

Risk: Generated page recreation is approximate and could unintentionally preserve reference-brand elements.

Mitigation: Keep the instruction to avoid source products, brand names, and logos, and review generated images before delivery or publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage when qhkit generation succeeds.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
