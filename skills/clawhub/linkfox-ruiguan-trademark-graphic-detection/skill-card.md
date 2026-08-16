## Description:

产品图片的图形商标检测与相似度搜索，用于将产品图片中的图形或 Logo 与多地区注册商标数据库进行相似度比对并辅助评估商标风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, brand owners, and agents use this skill to screen product images for visually similar registered graphic trademarks before listing or reviewing products. It helps summarize likely matches, similarity scores, trademark status, regions searched, and risk context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends product images and related metadata to LinkFox services for trademark screening.

Mitigation: Use only images and product metadata that are appropriate to share with LinkFox, and avoid submitting confidential or regulated content unless the user has approved that disclosure.

Risk: Local images may be uploaded as publicly accessible URLs before analysis.

Mitigation: Confirm that uploading the image is acceptable, avoid sensitive local files, and treat generated image URLs as shareable for their validity period.

Risk: The skill stores full API responses locally, which may include product image URLs, trademark matches, and account-related context.

Mitigation: Review saved LinkFox output files for sensitive data and remove or protect them according to the workspace's data-handling requirements.

Risk: The skill includes phone-login, API-key setup, paid plan ordering, and payment workflows.

Mitigation: Obtain and store API keys through trusted first-party LinkFox flows, avoid modified LINKFOX_* endpoint variables, and require explicit user approval before paid actions.

Risk: Trademark screening results can inform risk assessment but do not replace legal advice.

Mitigation: Present results as screening signals, explain similarity and status fields, and recommend qualified legal review for infringement or filing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-trademark-graphic-detection)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full LinkFox API responses to local JSON files, summarizes large responses, and may return public image URLs for uploaded local images.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
