## Description: <br>
将中文草稿整理为可对外发布的版本：清理创作标记、生成标题候选、简介和封面图，并输出独立发布目录，适用于文章、报告、教程、项目介绍和说明材料。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and editors use this skill to turn Chinese draft Markdown into publication-ready local outputs with cleaned body text, title options, a short summary, optional cover-image metadata, and versioned publish files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates local publish folders and appends changelog records. <br>
Mitigation: Review the target article path and publish version before approving side-effecting steps; keep the original draft unmodified. <br>
Risk: The optional cover-image workflow depends on wenqu-image, which may handle separate image generation or upload flows. <br>
Mitigation: Review wenqu-image separately before enabling cover generation, or skip cover generation and add a cover manually. <br>
Risk: Requests to automatically publish to external platforms are outside the current implemented behavior. <br>
Mitigation: Treat the skill output as a local publication package and manually review it before any external publishing. <br>


## Reference(s): <br>
- [发布流程](references/workflow.md) <br>
- [标题 / 简介写作规范](references/title-summary.md) <br>
- [封面图画图提示规范](references/cover-prompt.md) <br>
- [自动发布扩展点](references/auto-publish.md) <br>
- [Project homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-publish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown files plus concise text status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes versioned publish artifacts and changelog entries; optional cover image URL may be omitted if generation is unavailable.] <br>

## Skill Version(s): <br>
0.1.12 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
