## Description:

帮助 SHEIN 卖家和服装跨境独立站通过青虎 AI 生成商品主图套图、详情图、活动图、模特穿搭图、平铺图、细节图和多角度展示图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to prepare SHEIN-oriented fashion product imagery through qhkit, including main image sets, long-form detail images, and promotional posters. The skill guides model option lookup, cost estimation, user confirmation, generation, polling, and delivery of resulting image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may install and run unpinned qhkit or related image tooling in the user's environment.

Mitigation: Use a restricted workspace or a preinstalled, reviewed qhkit version before allowing generation workflows.

Risk: The workflow requires a Qinghu API token for paid generation services.

Mitigation: Configure the token through a secret manager or local environment variable instead of pasting credentials into chat.

Risk: Image generation can consume account credits.

Mitigation: Run cost estimation and get explicit user confirmation before any generate command creates a task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-shein-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cost estimates, confirmation prompts, qhkit status messages, generated image URLs, and credit usage.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
