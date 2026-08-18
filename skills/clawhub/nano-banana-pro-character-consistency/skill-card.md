## Description:

使用 Nano Banana Pro 在广告、社媒、短故事、虚拟模特和品牌 Campaign 中保持同一商业人物的脸、年龄、发型、体型、服装与身份连续。Use this skill for Nano Banana Pro character consistency、一致人物、虚拟模特、品牌代言人、数字人图片、连续场景、换装、表情动作表和系列广告；通过 AI Hive 使用人物参考图生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and creative teams use this skill to generate Nano Banana Pro image workflows that preserve a commercial character's face, age, hairstyle, body type, clothing, and identity across ads, social posts, short stories, virtual model shoots, and campaign scenes. Users should provide only approved reference images and confirm likeness rights before using generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to AI Hive for image generation.

Mitigation: Use only user-selected images that are approved for the intended channel, region, duration, and commercial use.

Risk: The AI Hive API key may be stored locally when the init command is used.

Mitigation: Store credentials with restricted file permissions, prefer environment variables where appropriate, and rotate the key if it may have been exposed.

Risk: Generated likenesses can create misleading endorsement, identity, or sensitive-context claims.

Mitigation: Require documented likeness authorization, label synthetic use when appropriate, and reject prompts that imply unauthorized endorsement, news events, or identity statements.

Risk: Character identity can drift across batches, outfits, or scenes.

Mitigation: Review outputs against the identity anchor, approved styling table, and scene log before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-character-consistency)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples; generated image task outputs are downloaded as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-selected reference images, AI Hive API credentials, optional batch size, routing, aspect ratio, output directory, and task ID inputs.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact CHANGELOG top entry lists 1.3.0 and should be reviewed)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
