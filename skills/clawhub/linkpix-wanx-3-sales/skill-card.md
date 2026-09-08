## Description:

This skill helps agents use Qinghu qhkit and LinkPix workflows to generate Taobao, Tmall, 1688, and Alimama-oriented ecommerce product videos with Alibaba Wanx 3.0 / Tongyi Wanxiang model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, agencies, and agent users can use this skill to plan and run product-video generation for Chinese marketplace listings, promotions, livestream teasers, and paid-ad creative. The skill guides model discovery, qhkit setup, media upload, task submission, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime installation of mutable third-party tooling can change behavior between runs.

Mitigation: Preinstall and pin a trusted qhkit version before deploying the skill, then review upgrades separately.

Risk: API keys may be exposed if pasted into chat or stored in logs.

Mitigation: Use environment variables or a secret manager with a narrowly scoped, revocable Qinghu token.

Risk: Product images, reference media, and generated-video prompts may be uploaded to an external service.

Mitigation: Use the skill only for media that is approved for Qinghu/qhkit/LinkPix processing and avoid sensitive or embargoed assets.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/autoagc/skills/linkpix-wanx-3-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce links or local paths for generated video outputs after qhkit task polling completes.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
