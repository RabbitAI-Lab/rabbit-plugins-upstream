## Description:

帮助拼多多运营、美工和卖家使用 qhkit/青虎 AI 生成主图套图、详情图、活动促销图、白底图和透明底图等电商图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, designers, and operations teams use this skill to prepare Pinduoduo-oriented product image workflows, including main-image sets, detail-page images, and promotional posters. It guides the agent through qhkit setup, model option lookup, estimate-before-generate confirmation, task submission, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses the external qhkit service and may upload product images.

Mitigation: Use only approved product assets and confirm that sharing them with qhkit is acceptable before submitting generation jobs.

Risk: The workflow requires a qhkit API key.

Mitigation: Store the API key through qhkit configuration or an environment variable, avoid exposing it in chat or logs, and rotate it if disclosure is suspected.

Risk: Image generation can consume paid qhkit credits.

Mitigation: Run the matching estimate command and obtain explicit user confirmation of model, image count, dimensions, reference images, and expected credits before generation.

Risk: The setup path may install Node.js or qhkit CLI dependencies.

Mitigation: Prefer the documented npm package path, verify downloaded Node.js archives with the published SHA256 file before extraction, and report installation failures to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pinduoduo-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON command parameters, and generated image result URLs when qhkit tasks complete]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit configuration; generation should be preceded by option lookup, credit estimate, and explicit user confirmation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
