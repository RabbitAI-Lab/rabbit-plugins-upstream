## Description:

LinkPix guides agents to generate ecommerce product images through the qhkit CLI, including main-image carousel sets, long detail-page images, and prompt-based commercial images with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, marketers, and agent developers use this skill to route product-image requests to the right LinkPix/qhkit image mode, prepare parameters, estimate credits, run generation, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and modify the Node environment.

Mitigation: Use a preinstalled, pinned qhkit binary when possible, or require explicit user approval before global installs and upgrades.

Risk: Product images and prompts are uploaded to the qhkit/LinkPix service.

Mitigation: Review inputs for confidential or regulated content before generation and avoid sending sensitive assets unless the service is approved for that data.

Risk: The skill can reuse an existing local OpenClaw qhkit token.

Mitigation: Confirm token use is authorized for the task and prefer scoped credentials where available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, credit estimates, and user-facing failure messages from the CLI.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
