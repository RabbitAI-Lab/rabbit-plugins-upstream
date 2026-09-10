## Description:

批量把商品图处理成干净的纯白底图：自动识别商品主体、去除杂乱背景，适配平台白底图规范。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents use this skill to turn product photos into clean white-background product images in batch workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade mutable qhkit command-line software.

Mitigation: Use a pinned, reviewed qhkit version and avoid executing upgrade commands copied from tool output without review.

Risk: Selected product images are uploaded to the service for processing.

Mitigation: Confirm the user's intent before sending images, especially for ambiguous cutout or background-removal requests.

Risk: The workflow uses a QHKIT token for service access.

Mitigation: Handle the token as a secret, prefer environment-based configuration, and avoid exposing it in user-visible output.

Risk: Generated white-background images may slightly change product details.

Mitigation: Ask the user to verify critical product details such as text, logos, and item structure before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, credit usage, and user-facing failure messages.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
