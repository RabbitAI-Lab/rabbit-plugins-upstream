## Description:

This skill helps agents use the qhkit CLI to batch convert product photos into clean white-background ecommerce images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting ecommerce teams use this skill to prepare product images for marketplace white-background requirements, including batch background removal, white-background generation, cost estimation, and delivery of generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/qhkit tooling in the execution environment.

Mitigation: Prefer a controlled environment with qhkit already installed, or require explicit approval before installing or upgrading tooling.

Risk: Product images are uploaded to the LinkPix/qhkit service for processing.

Mitigation: Confirm authorization before processing private, customer, or sensitive product images.

Risk: Image generation can spend service credits, especially in batch workflows.

Mitigation: Use qhkit estimate before generation and confirm credit availability and expected cost for larger batches.

Risk: The skill can reuse existing OpenClaw or QHKIT credentials.

Mitigation: Run under the intended account, avoid exposing tokens, and prefer scoped credentials when available.

Risk: Generated white-background images may slightly alter product details, text, logos, or structure.

Mitigation: Review generated outputs against the source images before publication or marketplace upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces white-background JPG or PNG bitmap image URLs through qhkit; transparent alpha output is outside the stated capability.]

## Skill Version(s):

0.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
