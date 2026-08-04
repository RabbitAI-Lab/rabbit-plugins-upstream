## Description: <br>
萃书根据输入的真实书名获取书籍素材，生成约100字简介、三个核心观点、五条行动建议和一张高质量中文信息图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xishaochen](https://clawhub.ai/user/xishaochen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to quickly understand a real book's core ideas and turn them into practical actions. It is intended for book essence extraction, concise summaries, action recommendations, and infographic generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs the agent to send a generated image through a local POPO file-transfer command without waiting for user confirmation. <br>
Mitigation: Show the generated image first and require explicit user approval before sending; limit the recipient and file path to the current request's generated image. <br>
Risk: Book summaries can be inaccurate when source material is unavailable or the skill relies on model knowledge. <br>
Mitigation: Label the material source or confidence level in the output and avoid presenting unsupported claims as sourced facts. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/xishaochen/skills/cuishu) <br>
- [Chinese Text Project](https://ctext.org/) <br>
- [Project Gutenberg ebook search](https://www.gutenberg.org/ebooks/search/) <br>
- [Douban Books](https://book.douban.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown summary with a generated image file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may generate a 1024x1536 infographic image and instructs a local POPO file-transfer command after generation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
