## Description:

根据商品信息快速生成广告视频素材，适用于信息流广告、品牌推广及社交媒体营销，支持多条量产。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and marketing operators use this skill to prepare batches of ecommerce video ad assets for feed ads, brand promotion, and social media campaigns. The skill guides an agent through qhkit setup, price estimation, user confirmation, task submission, polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can consume paid qhkit credits when video generation is submitted.

Mitigation: Run an estimate first, list the key generation parameters and estimated credits, and submit only after explicit user approval.

Risk: Referenced product images or videos may be uploaded to the LinkPix/qhkit service.

Mitigation: Confirm which local files or URLs will be used before submission and avoid including media the user has not approved for upload.

Risk: The setup path may install or upgrade the @iqinghu/qhkit package and use a qinghu token or QHKIT_TOKEN.

Mitigation: Install qhkit only when the user intends to use this paid video workflow, and rely on the configured token without exposing secrets in responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with qhkit CLI commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated video task IDs, status updates, final media URLs, and credit estimates or actual credit usage.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
