## Description:

AI 自动优化商品主图的构图、光影、质感及细节，提升商品吸引力与点击率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to guide an agent through improving product listing images with LinkPix/qhkit, including model selection, credit estimation, image generation, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may install npm or Python image tooling during setup.

Mitigation: Install only in an environment where adding qhkit and image-processing utilities is acceptable, and review installation prompts or errors before continuing.

Risk: The workflow uploads selected product images to the qhkit service.

Mitigation: Use only images that are approved for processing by that service and verify generated outputs for product text, logos, and structural details.

Risk: The skill may require configuring a qhkit API token locally.

Mitigation: Prefer scoped or revocable credentials and avoid sharing long-lived or broadly privileged API keys.

Risk: Image generation can consume service credits.

Mitigation: Run the estimate step and obtain explicit user approval before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix login and API key setup](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to install qhkit, configure a qhkit API token, estimate credits, and submit image generation jobs after user confirmation.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
