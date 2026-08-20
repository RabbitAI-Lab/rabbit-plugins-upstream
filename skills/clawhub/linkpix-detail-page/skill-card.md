## Description:

Generates ordered e-commerce product detail-page image sets from a required product reference image using the qhkit CLI, with optional theme selection and custom sales copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to turn product images into detail-page image sets for listings, refreshes, and product presentation workflows. Agents use it to estimate qhkit credit cost, generate the images, and return the resulting image URLs with actual credits consumed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to install qhkit or Node globally and modify PATH.

Mitigation: Review install commands before execution and prefer environments where qhkit and Node are already installed.

Risk: The skill can reuse local OpenClaw/qhkit credentials or require a qhkit token.

Mitigation: Approve credential use explicitly and avoid running it where unintended local credentials are present.

Risk: The skill uploads product images to an external service and may spend qhkit credits.

Mitigation: Confirm image-upload permission and run qhkit estimate before generation when credit cost matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and returned image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ordered product-detail image URLs and reports actual qhkit credits consumed.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
