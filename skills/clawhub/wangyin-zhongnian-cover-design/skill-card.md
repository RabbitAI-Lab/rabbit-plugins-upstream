## Description: <br>
为公众号「网瘾中年」生成 2.35:1 横版封面提示词，基于品牌机器人 IP、工程蓝 VI 规范和 NVH 频率曲线视觉符号，通过三轮问答输出可用于多参考图生图模型的中文提示词。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shun1989](https://clawhub.ai/user/shun1989) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Content creators and agents use this skill to turn a WeChat public-account article into a branded 2.35:1 cover-image prompt. It guides style selection, reference-image planning, visual-detail choices, and final prompt generation for image models such as Seedream, Nano Banana, or GPT-Image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional direct-generation script can send prompts and reference images to Volcengine ARK. <br>
Mitigation: Use the prompt-only workflow by default, and run the script only after confirming the prompt, reference images, and third-party processing expectations. <br>
Risk: The optional script reads local image-generation API credentials from ~/.baoyu-skills/.env. <br>
Mitigation: Keep the credential file private, verify which API key will be used, and avoid running the script in shared or untrusted environments. <br>
Risk: Private screenshots or images used as references may be uploaded to a third-party image-generation service. <br>
Mitigation: Do not pass sensitive screenshots or private reference images with --ref unless external processing is acceptable. <br>
Risk: Generated covers may contain incorrect Chinese title text or a robot IP that drifts from the required proportions and colors. <br>
Mitigation: Review each generated image for title accuracy, robot shape, brand colors, and forbidden visual elements before publication; regenerate or locally edit failures. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shun1989/skills/wangyin-zhongnian-cover-design) <br>
- [README](artifact/README.md) <br>
- [Skill Instructions](artifact/SKILL.md) <br>
- [Brand Visual Constraints](artifact/references/vi-constraints.md) <br>
- [Prompt Examples](artifact/references/examples.md) <br>
- [Optional Volcengine ARK API Endpoint](https://ark.cn-beijing.volces.com/api/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style Chinese prompt text with optional configuration notes and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final prompts target 2.35:1 WeChat cover images, preserve the specified robot IP constraints, and may reference multiple input images when the selected image model supports them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
