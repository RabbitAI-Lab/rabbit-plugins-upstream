## Description:

Guides an agent through Qinghu AI's paid workflow to generate cinematic TVC-style product advertising videos from 1-8 product images, product details, language, and aspect-ratio choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and agents use this skill to collect product inputs, estimate paid Qinghu AI credits, submit a TVC advertising video workflow, poll for completion, and return the generated video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and product details may be uploaded to Qinghu AI during video generation.

Mitigation: Confirm the user intends to use Qinghu AI and that the submitted product assets and details are appropriate to upload before running the workflow.

Risk: The workflow uses paid credits and has a cost-confirmation step before generation.

Mitigation: Run the estimate command with the final parameters, report the quoted credit cost, and wait for user approval before submitting generation.

Risk: Using product images without rights can create commercial-use or intellectual-property risk.

Mitigation: Use only images the user owns or is authorized to use commercially.

Risk: API-token configuration is required for qhkit access.

Mitigation: Use the configured qhkit token only for the intended workflow and avoid exposing token values in user-facing output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns workflow setup guidance, parameter JSON, cost-confirmation steps, polling instructions, and generated video URLs when available.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
