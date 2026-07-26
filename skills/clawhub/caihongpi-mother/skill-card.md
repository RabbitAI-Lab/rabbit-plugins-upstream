## Description: <br>
根据用户分享的当妈真实经历或场景，生成走心夸夸卡内容、Gemini 文生图提示词，以及小红书、抖音、快手三平台发布信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongzichixiangjiao](https://clawhub.ai/user/kongzichixiangjiao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this Chinese-language skill to turn parenting experiences into praise-card copy, image-generation prompts, and platform-specific posting guidance. It supports active praise requests and passive emotion-aware suggestions that require user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated parenting content may include child, family, health, location, or other private details supplied by the user. <br>
Mitigation: Review and remove private details before public posting, as directed by the security guidance and the skill's privacy notice. <br>
Risk: Generated prompts and README files can persist sensitive parenting content on local disk after saving. <br>
Mitigation: The skill requires explicit save confirmation, shows the target path before writing, and allows users to decline local file creation. <br>
Risk: Emotion-aware triggering could be intrusive if praise content starts from a passive signal alone. <br>
Mitigation: The artifact limits triggering to parenting contexts and requires explicit user agreement before entering the praise-generation workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongzichixiangjiao/skills/caihongpi-mother) <br>
- [README.md](artifact/README.md) <br>
- [Main skill definition](artifact/SKILL.md) <br>
- [Emotion detector reference](artifact/references/01-情绪识别器/SKILL.md) <br>
- [Image prompt writer reference](artifact/references/02-文生图提示词写手/SKILL.md) <br>
- [Style adapter reference](artifact/references/03-风格适配器/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown conversation output plus Prompt .txt files and README.md when local saving is confirmed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates Chinese praise copy, English Gemini image prompts, platform posting metadata, and a posting assembly guide; local files are written only after user confirmation.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
