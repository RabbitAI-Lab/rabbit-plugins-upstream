## Description: <br>
Markdown 排版工具箱。格式化中文混排、转换微信公众号/小红书格式、生成目录、检查链接和标题层级。当用户需要排版、美化、转换 Markdown 文件时使用本技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krisyhr](https://clawhub.ai/user/krisyhr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and developers use this skill to format Markdown documents for Chinese-English typography, convert Markdown for WeChat publishing, work with Markdown tables, generate tables of contents, inspect links, and count document text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-named local documents and can create derived output files beside the originals. <br>
Mitigation: Run commands only on intended paths and review generated Markdown, HTML, CSV, or formatted files before publishing or sharing. <br>
Risk: Converted output may contain content derived from sensitive documents. <br>
Mitigation: Avoid running conversion commands on sensitive documents unless derived local output files are acceptable. <br>


## Reference(s): <br>
- [Markdown Chinese Formatting Rules](references/format-rules.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/krisyhr/skills/markdown-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples; commands produce formatted Markdown, HTML, CSV, tables of contents, link lists, or text statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local file operations read explicit document paths and may write derived files next to the originals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
