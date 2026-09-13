## Description:

帮助淘宝和天猫运营、设计和品牌团队使用 LinkPix/qhkit 生成商品主图套图、详情页长图、SKU 图、促销海报和活动图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, designers, and brand visual teams use this skill to prepare Taobao/Tmall product images, carousel sets, detail-page images, SKU images, promotional posters, and campaign graphics. The skill guides an agent through qhkit setup, option discovery, cost estimation, confirmation, generation, and delivery of image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to provide or configure API credentials.

Mitigation: Do not paste API keys into chat; prefer a protected secret store or local environment variable with revocable scoped tokens.

Risk: Product images and prompts may be sent to the Qinghu/qhkit service.

Mitigation: Use the skill only when sharing those images and prompts with that service is acceptable for the user's confidentiality, rights, and policy requirements.

Risk: The setup path can install mutable third-party tooling globally.

Mitigation: Prefer contained execution environments and pinned dependency versions when deploying or reviewing the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-taobao-tmall-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead an agent to call qhkit, which returns JSON status, credit usage, and generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
