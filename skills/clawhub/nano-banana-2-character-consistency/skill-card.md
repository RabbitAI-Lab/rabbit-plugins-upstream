## Description:

使用 Nano Banana 2 为品牌 IP、虚拟人物、绘本、社交内容和连续分镜保持角色身份、服装、配色与标志物一致。Use this skill for Nano Banana 2角色一致性、品牌吉祥物、IP形象、虚拟人、社媒系列、绘本角色、漫画人物、表情包和连续场景；通过 AI Hive 使用角色参考图生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand teams, and developers use this skill to generate Nano Banana 2 character-consistent image assets from approved reference images for mascots, virtual characters, social series, sticker sets, wardrobe variants, and storyboard continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key.

Mitigation: Use a scoped key where possible, keep it out of shared prompts and logs, and review local configuration before use.

Risk: Reference images selected by the user are uploaded to AI Hive/object storage.

Mitigation: Use only approved, non-sensitive, and properly licensed reference images.

Risk: Generated outputs are saved locally.

Mitigation: Review the configured output directory and remove generated files that should not be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-character-consistency)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; the CLI emits JSON task status and downloads generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; uploads user-selected reference images and saves generated outputs locally unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
