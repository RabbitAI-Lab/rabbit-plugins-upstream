## Description: <br>
Daily Tongjian helps an agent deliver a bilingual daily reading experience for Zizhi Tongjian, with tracked progress, full lecture text, scene art guidance, and voice narration guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yumyumtum](https://clawhub.ai/user/yumyumtum) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn Zizhi Tongjian into a daily lecture series with original-text excerpts, translation, commentary, scene-image direction, voice narration direction, and replay-friendly local archives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update reading progress and save generated lecture text, images, and audio under ~/.openclaw. <br>
Mitigation: Use explicit prompts such as "今日通鉴" or "继续读通鉴", review status before advancing, and manage or delete local replay files when retention is not desired. <br>
Risk: Lecture content is generated from the agent's knowledge rather than a bundled full-text source. <br>
Mitigation: Review important historical excerpts, translations, and commentary against trusted editions before relying on them for publication or instruction. <br>


## Reference(s): <br>
- [Daily Tongjian ClawHub listing](https://clawhub.ai/yumyumtum/skills/daily-tongjian) <br>
- [Daily Tongjian Structure Guide](references/structure.md) <br>
- [Daily Tongjian Style Guide](references/style-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown lecture content with inline bash commands and local progress or replay file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update ~/.openclaw/workspace/daily-tongjian/progress.json and save replay text, image, and audio files under ~/.openclaw/media/outbound.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
