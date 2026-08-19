## Description:

Create and edit Amazon catalog images, PDP galleries, A+ Content modules, Brand Store heroes, variant sets and advertising creative bases. Use this skill for Amazon商品图、亚马逊Listing、A+页面、品牌旗舰店、主图、信息图、包装清单、尺寸比例、Sponsored Ads素材和多站点本地化；supports AI Hive reference generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and creative teams use this skill to plan and generate Amazon catalog, PDP, A+ Content, Brand Store, localization, and advertising image assets from approved product and brand references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product, packaging, and brand assets are sent to AI Hive during generation.

Mitigation: Review each file before upload and use only assets that the seller has rights to share with the service.

Risk: The AI Hive API key is stored locally or passed through the environment.

Mitigation: Store the API key with restricted file permissions, avoid committing it, and rotate it if exposure is suspected.

Risk: The upload helper does not enforce image-only extensions.

Mitigation: Limit uploads to intended product and brand reference files before invoking the skill.

Risk: Generated Amazon creative could include unapproved commercial claims, ratings, badges, certifications, prices, or competitor comparisons.

Mitigation: Check outputs against the seller source sheet and current marketplace requirements before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/amazon-ecommerce-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; the CLI can submit AI Hive generation tasks and download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied product, packaging, and brand reference assets; generated files default to the AI Hive download directory unless the user overrides the output path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
