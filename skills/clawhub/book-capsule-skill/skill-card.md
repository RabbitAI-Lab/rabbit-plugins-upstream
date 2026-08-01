## Description: <br>
浓缩一本好书的精华，像胶囊一样随取随用。输入一个作者或一本书，生成精美卡片式书摘文章，存到本地或推送到公众号，帮你对抗遗忘、碎片阅读、为自己的书架留痕。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and content creators use this skill to turn a book, author, or prepared JSON data into a local card-style HTML reading capsule for review, sharing, or publication workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes temporary JSON and output HTML files and runs a local Python renderer. <br>
Mitigation: Install only if this local file-writing and command-execution workflow is acceptable, and review generated files before use. <br>
Risk: Untrusted quote or book metadata can appear in the generated HTML. <br>
Mitigation: Avoid placing untrusted HTML or script-like text in quote fields unless that output is intended, and review generated HTML before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/book-capsule-skill) <br>
- [README.md](README.md) <br>
- [template-usage.md](template-usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON structure and shell command examples; final artifact is a local HTML file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON input and a bundled Python renderer; generated HTML should be reviewed before publication.] <br>

## Skill Version(s): <br>
0.1.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
