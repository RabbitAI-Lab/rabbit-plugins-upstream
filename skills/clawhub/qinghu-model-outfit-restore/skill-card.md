## Description:

Uploads a model image and garment image to Qinghu AI through qhkit to generate a high-consistency virtual try-on result that preserves pose, lighting, and clothing detail for ecommerce outfit imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to place a selected garment onto a model image while preserving the original pose and lighting. It guides setup, price estimation, submission, polling, and delivery for the Qinghu AI virtual try-on workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected local model and garment images to the Qinghu external service.

Mitigation: Use only images the user owns or has permission to process, and avoid sensitive or unauthorized personal imagery.

Risk: The workflow can spend Qinghu credits after estimate confirmation.

Mitigation: Run the estimate step with the exact generation parameters, disclose the returned credits, and wait for confirmation before submitting.

Risk: The skill may install Node/qhkit tooling and requires a Qinghu token or configuration.

Mitigation: Install qhkit from the documented package source, verify the workflow command is available, and handle API tokens through the documented config or environment mechanisms.

Risk: Online workflow fields can change from the documented 2026-08 snapshot.

Mitigation: Run the options command before uncertain submissions and copy returned field labels and choices exactly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline bash and JSON examples; runtime CLI responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow returns generated image URLs after polling, and final user-facing responses include actual credit consumption when a task succeeds.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
