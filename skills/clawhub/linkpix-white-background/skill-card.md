## Description:

批量把商品图处理成干净的纯白底图：自动识别商品主体、去除杂乱背景，适配平台白底图规范。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to guide agents through installing qhkit, estimating paid generation cost, and producing white-background product images in batches for marketplace listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are sent to the LinkPix/qhkit service for processing.

Mitigation: Use the skill only with images appropriate for that service and avoid submitting sensitive or unauthorized product imagery.

Risk: The skill may require storing or providing an API token.

Mitigation: Use the qhkit token configuration or QHKIT_TOKEN environment variable and avoid exposing tokens in shared logs, prompts, or committed files.

Risk: Generate actions may consume credits.

Mitigation: Run the estimate action first and require explicit user approval before submitting any paid generation request.

Risk: Generated white-background images may differ slightly from the source product details.

Mitigation: Review generated outputs for critical product details such as text, logos, and structure before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may trigger qhkit image-batch estimate, options, and generate commands; generated outputs are white-background JPG or PNG product images returned by the LinkPix/qhkit service.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
