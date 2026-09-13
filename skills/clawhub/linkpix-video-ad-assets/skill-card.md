## Description:

根据商品信息快速生成广告视频素材，适用于信息流广告、品牌推广及社交媒体营销，支持多条量产。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and agent users use this skill to generate multiple LinkPix video ad assets from product descriptions and product images for feed ads, social campaigns, and brand promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install or upgrade an unpinned global qhkit CLI.

Mitigation: Use an isolated environment and a pinned qhkit version unless a reviewed upgrade is required.

Risk: The skill requires a LinkPix/qhkit API token and may persist credentials.

Mitigation: Use platform-managed secrets or environment variables and avoid exposing tokens in prompts, logs, or shell history.

Risk: Video generation sends selected product media to the LinkPix/qhkit service and consumes credits.

Mitigation: Confirm media sharing is acceptable and run an estimate before submitting generation requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit video generation, cost estimation, status polling, credential configuration, and delivery of generated video URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
