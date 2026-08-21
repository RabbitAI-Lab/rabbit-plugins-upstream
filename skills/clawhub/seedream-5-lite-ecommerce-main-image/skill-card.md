## Description:

使用 Seedream 5.0 Lite 通过商品事实、渠道规范、缩略图识别和促销合规四道闸门制作电商主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and developers use this skill to generate Seedream 5.0 Lite product-main-image candidates for marketplace listings while checking SKU facts, channel presentation rules, thumbnail legibility, and promotional claims before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses an AI Hive API key and can upload product or reference images selected by the user.

Mitigation: Use an appropriate scoped API key where available, keep the local config file private, and upload only assets approved for the target workflow.

Risk: Generated ecommerce images may still conflict with SKU facts, marketplace rules, or promotional-compliance requirements.

Mitigation: Review each output against the SKU record, packing list, target channel rules, thumbnail view, and approved claims before publishing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, JSON configuration, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are saved locally by the helper script; task lookup can return JSON status from AI Hive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
